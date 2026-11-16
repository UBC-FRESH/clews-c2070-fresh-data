#!/usr/bin/env python3
"""Generate diagnostic plots for the TSA24 DBH distribution fits.

By default the figures are built from the working-tree CSVs and JSON, so a
fresh spike re-fit is reflected without a commit.  Pass ``--committed`` to
snapshot ``git show HEAD:...`` instead.  The tracking script reconstructs the
selected PDFs with SciPy and loads the raw FAIB PSP tree list through the
committed or working-tree ``validate_tsa24`` loader.

Run with the repository virtual environment and a nemora checkout on
``PYTHONPATH``::

    NEMORA_ROOT=/srv/shared-data/gep/ws4/nemora \
      .venv/bin/python data/derived/national/assortments/tsa24_prototype/plots/make_plots.py

The script writes five PNGs into this directory.  It never writes to the
existing prototype CSVs.
"""

from __future__ import annotations

import argparse
import io
import json
import math
import os
import subprocess
import sys
import tarfile
import tempfile
from collections.abc import Mapping, Sequence
from pathlib import Path
from typing import Any

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.axes import Axes
from matplotlib.patches import Patch
from scipy.stats import gamma as gamma_dist
from scipy.stats import weibull_min

# Directory layout: .../clews-c2070-fresh/data/derived/.../tsa24_prototype/plots
PLOT_DIR = Path(__file__).resolve().parent
DATA_ROOT = PLOT_DIR.parents[4]
REPO_ROOT = PLOT_DIR.parents[5]
PROTOTYPE_REL = Path("derived/national/assortments/tsa24_prototype")

SPECIES_ORDER = ("AT", "BL", "EP", "FD", "PL", "SB", "SW")
SPECIES_NAMES = {
    "AT": "Trembling aspen",
    "BL": "Subalpine fir",
    "EP": "Paper birch",
    "FD": "Douglas-fir",
    "PL": "Lodgepole pine",
    "SB": "Black spruce",
    "SW": "White spruce",
    "CW": "Western redcedar",
}
DISTRIBUTION_LABELS = {
    "mixture": "two-gamma mixture",
    "mix_weibull_2": "2-Weibull mixture",
    "mix_weibull_gamma": "Weibull+gamma mixture",
    "weibull": "Weibull",
    "gamma": "gamma",
    "gb1": "generalized beta 1",
    "gb2": "generalized beta 2",
    "spike_weibull": "spike Weibull (diagnostic)",
    "spike_gamma": "spike gamma (diagnostic)",
    "spike_weibull_constrained": "constrained spike Weibull",
    "spike_gamma_constrained": "constrained spike gamma",
}
SHORT_DISTRIBUTION_LABELS = {
    "mixture": "2-gamma",
    "mix_weibull_2": "2-Weibull",
    "mix_weibull_gamma": "W+gamma",
    "weibull": "Weibull",
    "gamma": "gamma",
    "spike_weibull": "spike W",
    "spike_gamma": "spike γ",
    "spike_weibull_constrained": "spike W c",
    "spike_gamma_constrained": "spike γ c",
}

SPIKE_COMPONENTS = {
    "spike_weibull": "weibull",
    "spike_gamma": "gamma",
    "spike_weibull_constrained": "weibull",
    "spike_gamma_constrained": "gamma",
}
CW_HIGH_KS_FITS = (
    ("ecozone", "Montane Cordillera"),
    ("ecoprovince", "Columbia Montane Cordillera"),
)

COLORS = {
    "observed_fill": "#A9BFCC",
    "observed_edge": "#5F7487",
    "selected": "#B23A2E",
    "candidate_weibull": "#2C6E9B",
    "candidate_gamma": "#7A4E9E",
    "accent": "#0F766E",
    "ink": "#1F2937",
    "muted": "#4B5563",
    "grid": "#E5E7EB",
    "sawlog": "#1F6F5C",
    "pulpwood": "#D97706",
    "other": "#64748B",
    "residue": "#8B5E3C",
}

plt.rcParams.update(
    {
        "figure.dpi": 200,
        "savefig.dpi": 200,
        "savefig.bbox": "tight",
        "savefig.pad_inches": 0.16,
        "font.family": "DejaVu Sans",
        "font.size": 9,
        "axes.titlesize": 11,
        "axes.labelsize": 9,
        "axes.edgecolor": COLORS["muted"],
        "axes.labelcolor": COLORS["ink"],
        "axes.titlecolor": COLORS["ink"],
        "axes.spines.top": False,
        "axes.spines.right": False,
        "axes.grid": True,
        "axes.axisbelow": True,
        "grid.color": COLORS["grid"],
        "grid.linewidth": 0.65,
        "xtick.color": COLORS["muted"],
        "ytick.color": COLORS["muted"],
        "text.color": COLORS["ink"],
        "legend.frameon": True,
        "legend.framealpha": 0.95,
        "legend.edgecolor": "#CBD5E1",
    }
)


# ---------------------------------------------------------------------------
# Committed-artifact boundary
# ---------------------------------------------------------------------------


def _git_show(repo: Path, repo_relative_path: Path) -> bytes:
    """Return one committed file as bytes, never the working-tree version."""
    result = subprocess.run(
        ["git", "-C", str(repo), "show", f"HEAD:{repo_relative_path.as_posix()}"],
        check=False,
        capture_output=True,
    )
    if result.returncode != 0:
        detail = result.stderr.decode("utf-8", errors="replace").strip()
        raise RuntimeError(
            f"cannot read committed artifact {repo_relative_path} from {repo}: {detail}"
        )
    return result.stdout


def _working_artifact(data_root: Path, name: str) -> Path:
    path = data_root / PROTOTYPE_REL / name
    if not path.exists():
        raise RuntimeError(f"working-tree artifact not found: {path}")
    return path


def read_csv_artifact(
    data_root: Path, name: str, *, working: bool = False
) -> pd.DataFrame:
    if working:
        return pd.read_csv(_working_artifact(data_root, name), low_memory=False)
    payload = _git_show(data_root, PROTOTYPE_REL / name)
    return pd.read_csv(io.BytesIO(payload), low_memory=False)


def read_json_artifact(
    data_root: Path, name: str, *, working: bool = False
) -> dict[str, Any]:
    if working:
        return json.loads(_working_artifact(data_root, name).read_text(encoding="utf-8"))
    payload = _git_show(data_root, PROTOTYPE_REL / name)
    return json.loads(payload.decode("utf-8"))


def read_committed_csv(data_root: Path, name: str) -> pd.DataFrame:
    """Backward-compatible committed-snapshot reader used by the diagnostic."""
    return read_csv_artifact(data_root, name, working=False)


def read_committed_json(data_root: Path, name: str) -> dict[str, Any]:
    return read_json_artifact(data_root, name, working=False)


def load_observed_trees(
    repo_root: Path, data_root: Path, *, working: bool = False
) -> pd.DataFrame:
    """Load the TSA24 FAIB PSP live-tree subset.

    ``working=False`` imports the loader from a ``git archive HEAD`` snapshot;
    ``working=True`` imports it from the repository working tree so the plot
    and the re-fit always share one loader.
    """
    nemora_root = Path(
        os.environ.get("NEMORA_ROOT", "/srv/shared-data/gep/ws4/nemora")
    ).expanduser()
    nemora_src = nemora_root / "src"
    if not (nemora_src / "nemora").is_dir():
        raise RuntimeError(
            f"nemora source not found at {nemora_src}; set NEMORA_ROOT to a "
            "checkout containing src/nemora"
        )
    if working:
        sys.path.insert(0, str(nemora_src))
        sys.path.insert(0, str(repo_root))
        from workflows.national.assortments.validate_tsa24 import load_tsa24_data

        data = load_tsa24_data(repo_root, data_root, tsa_name="Prince George")
        return data.trees.copy()

    archive = subprocess.run(
        ["git", "-C", str(repo_root), "archive", "HEAD", "workflows"],
        check=False,
        capture_output=True,
    )
    if archive.returncode != 0:
        detail = archive.stderr.decode("utf-8", errors="replace").strip()
        raise RuntimeError(f"cannot archive committed workflows: {detail}")

    with tempfile.TemporaryDirectory(prefix="tsa24-head-workflows-") as tmp:
        with tarfile.open(fileobj=io.BytesIO(archive.stdout), mode="r:") as bundle:
            bundle.extractall(tmp, filter="data")
        sys.path.insert(0, str(nemora_src))
        sys.path.insert(0, tmp)
        from workflows.national.assortments.validate_tsa24 import load_tsa24_data

        data = load_tsa24_data(repo_root, data_root, tsa_name="Prince George")
        return data.trees.copy()


# ---------------------------------------------------------------------------
# Distribution reconstruction
# ---------------------------------------------------------------------------


def parse_components(row: pd.Series) -> list[tuple[str, float, dict[str, float]]]:
    """Parse one fit row into ``(component name, weight, parameters)``."""
    if str(row["distribution"]) in SPIKE_COMPONENTS:
        raise ValueError(
            f"fit {row['fit_id']} is a spike two-part model; use spike_curve"
        )
    payload = json.loads(row["parameters_json"]) if row["parameters_json"] else {}
    if not payload:
        raise ValueError(f"fit {row['fit_id']} has no parameters to plot")

    if "components" not in payload:
        return [(str(row["distribution"]), 1.0, dict(payload))]

    components = [
        (
            str(component["name"]),
            float(component["weight"]),
            {str(key): float(value) for key, value in component["parameters"].items()},
        )
        for component in payload["components"]
    ]
    total_weight = sum(weight for _, weight, _ in components)
    if not math.isfinite(total_weight) or total_weight <= 0.0:
        raise ValueError(f"fit {row['fit_id']} has invalid mixture weights")
    return [
        (name, weight / total_weight, parameters)
        for name, weight, parameters in components
    ]


def spike_row_spec(
    row: pd.Series,
) -> tuple[float, float, str, dict[str, float]]:
    """Return ``(spike weight, width cm, component, component parameters)``."""
    distribution = str(row["distribution"])
    if distribution not in SPIKE_COMPONENTS:
        raise ValueError(f"fit {row['fit_id']} is not a spike model")
    payload = json.loads(row["parameters_json"]) if row["parameters_json"] else {}
    try:
        weight = float(payload["spike_weight"])
        width = float(payload["spike_bin_width"])
    except KeyError as error:
        raise ValueError(
            f"fit {row['fit_id']} lacks spike_weight/spike_bin_width"
        ) from error
    continuous = {
        key: float(value)
        for key, value in payload.items()
        if key not in {"spike_weight", "spike_bin_width"}
    }
    return weight, width, SPIKE_COMPONENTS[distribution], continuous


def spike_curve(
    row: pd.Series,
    *,
    upper_cm: float = 80.0,
    points: int = 1601,
) -> tuple[np.ndarray, np.ndarray, float]:
    """Return tail density above the first bin and the first-bin mass.

    The spike is a point mass reported as uniform inside the first bin.  A
    density curve cannot represent it, so the caller draws the returned
    ``spike_mass`` as a bar over the first bin and uses the tail density for
    everything above the first-bin upper edge.
    """
    weight, width, component, parameters = spike_row_spec(row)
    lower = float(row["dbh_limit_cm"])
    edge1 = lower + width
    values = np.linspace(0.0, upper_cm, points)
    retained = 1.0 - float(component_cdf(component, parameters, np.array([edge1]))[0])
    if not math.isfinite(retained) or retained <= 1e-12:
        raise ValueError(f"fit {row['fit_id']} has no retained tail mass")
    density = np.zeros_like(values, dtype=float)
    above = values >= edge1
    density[above] = (
        (1.0 - weight)
        * component_pdf(component, parameters, values[above])
        / retained
    )
    return values, density, weight


def spike_boundary_text(row: pd.Series) -> str:
    """Return the boundary status for a spike row, with old-CSV fallback."""
    status = str(row.get("spike_boundary_status") or "")
    at_bound = str(row.get("spike_at_bound") or "")
    if not status:
        payload = str(row.get("fit_diagnostics") or "")
        if payload:
            try:
                diagnostics = json.loads(payload)
            except json.JSONDecodeError:
                diagnostics = {}
            status = str(diagnostics.get("boundary_status") or "")
            at_bound = ",".join(str(item) for item in diagnostics.get("at_bound", []))
    if not status:
        status = "ok"
    if status == "ok":
        return "interior"
    return f"{status} ({at_bound or 'bound'})"


def component_pdf(
    name: str, parameters: Mapping[str, float], values: np.ndarray
) -> np.ndarray:
    if name == "weibull":
        return weibull_min.pdf(values, parameters["a"], scale=parameters["beta"])
    if name == "gamma":
        return gamma_dist.pdf(values, parameters["p"], scale=parameters["beta"])
    raise ValueError(f"cannot reconstruct PDF for component {name!r}")


def component_cdf(
    name: str, parameters: Mapping[str, float], values: np.ndarray
) -> np.ndarray:
    if name == "weibull":
        return weibull_min.cdf(values, parameters["a"], scale=parameters["beta"])
    if name == "gamma":
        return gamma_dist.cdf(values, parameters["p"], scale=parameters["beta"])
    raise ValueError(f"cannot reconstruct CDF for component {name!r}")


def conditional_pdf(
    components: Sequence[tuple[str, float, Mapping[str, float]]],
    lower_cm: float,
    values: np.ndarray,
) -> np.ndarray:
    """Evaluate the selected PDF conditioned on ``DBH >= lower_cm``.

    The fitting layer renormalises the mixture by the mass retained above the
    plot DBH limit.  This is the same convention used for the reported KS
    statistic, so the plotted curve lines up with the annotation.
    """
    retained = sum(
        weight * (1.0 - float(component_cdf(name, params, np.array([lower_cm]))[0]))
        for name, weight, params in components
    )
    if not math.isfinite(retained) or retained <= 1.0e-12:
        raise ValueError(f"selected fit has no mass above {lower_cm:g} cm")

    density = sum(
        weight * component_pdf(name, params, np.maximum(values, lower_cm))
        for name, weight, params in components
    )
    density = np.asarray(density, dtype=float) / retained
    return np.where(values >= lower_cm, density, 0.0)


def fit_pdf_on_grid(
    row: pd.Series, *, upper_cm: float = 80.0, points: int = 1601
) -> tuple[np.ndarray, np.ndarray]:
    lower_cm = float(row["dbh_limit_cm"])
    values = np.linspace(0.0, upper_cm, points)
    components = parse_components(row)
    return values, conditional_pdf(components, lower_cm, values)


def observed_counts(
    trees: pd.DataFrame, *, bin_width_cm: float = 2.0, upper_cm: float = 80.0
) -> tuple[np.ndarray, np.ndarray]:
    if trees.empty:
        raise ValueError("cannot histogram an empty tree subset")
    if float(trees["dbh_cm"].max()) > upper_cm:
        raise ValueError(
            f"observed DBH {trees['dbh_cm'].max():.1f} cm exceeds plot range {upper_cm:g} cm"
        )
    edges = np.arange(0.0, upper_cm + bin_width_cm + 1.0e-9, bin_width_cm)
    counts, _ = np.histogram(
        trees["dbh_cm"].to_numpy(dtype=float),
        bins=edges,
        weights=trees["expansion_factor"].to_numpy(dtype=float),
    )
    return edges, counts


def distribution_label(row: pd.Series) -> str:
    base = DISTRIBUTION_LABELS.get(str(row["distribution"]), str(row["distribution"]))
    if not bool(row.get("converged", True)):
        return f"{base} (non-converged fallback)"
    return base


def style_panel(ax: Axes, *, xlabel: bool, ylabel: bool) -> None:
    ax.set_xlim(0.0, 80.0)
    if xlabel:
        ax.set_xlabel("DBH (cm)")
    if ylabel:
        ax.set_ylabel("Trees ha$^{-1}$ per 2 cm")
    ax.tick_params(length=3, width=0.7)


# ---------------------------------------------------------------------------
# Figure 1: one panel per AU species
# ---------------------------------------------------------------------------


def plot_au_fits(
    fits: pd.DataFrame,
    trees: pd.DataFrame,
    target_stand: Mapping[str, Any],
    output_path: Path,
    *,
    source_label: str = "working-tree",
) -> None:
    au_fits = fits[
        (fits["scope"] == "tsa24_au_age_window") & (fits["selected"] == True)
    ].copy()
    if set(au_fits["species"]) != set(SPECIES_ORDER):
        raise ValueError(
            f"expected AU fits for {SPECIES_ORDER}, got {sorted(au_fits['species'])}"
        )

    fig, axes = plt.subplots(2, 4, figsize=(15.2, 7.7), sharex=True)
    flat_axes = axes.ravel()
    species_weights = target_stand["species_weights"]
    selected_handles: list[Any] = []
    spike_handle: Any | None = None

    for ax, species in zip(flat_axes[:7], SPECIES_ORDER, strict=True):
        row = au_fits[au_fits["species"] == species].iloc[0]
        subset = trees[
            trees["mapped"]
            & trees["species"].eq(species)
            & trees["ecodistrict"].eq("Nechako Lowland")
            & trees["age"].between(80.0, 120.0)
        ].copy()

        edges, counts = observed_counts(subset)
        centers = 0.5 * (edges[:-1] + edges[1:])
        ax.bar(
            centers,
            counts,
            width=1.82,
            align="center",
            color=COLORS["observed_fill"],
            edgecolor=COLORS["observed_edge"],
            linewidth=0.5,
            label="Observed PSP (expansion-weighted)",
            zorder=2,
        )

        total_weight = float(subset["expansion_factor"].sum())
        spike_peak = 0.0
        line_label = "Selected fit (conditional PDF)"
        if str(row["distribution"]) in SPIKE_COMPONENTS:
            values, density, spike_mass = spike_curve(row)
            scaled_density = density * total_weight * 2.0
            spike_peak = total_weight * spike_mass
            ax.bar(
                [float(row["dbh_limit_cm"]) + float(spike_row_spec(row)[1]) / 2.0],
                [spike_peak],
                width=1.82,
                color=COLORS["selected"],
                alpha=0.32,
                edgecolor=COLORS["selected"],
                hatch="//",
                linewidth=0.6,
                label="Selected spike mass (first bin)",
                zorder=3,
            )
            line_label = "Selected spike tail (1 − w)·PDF"
            if spike_handle is None:
                spike_handle = Patch(
                    facecolor=COLORS["selected"],
                    edgecolor=COLORS["selected"],
                    alpha=0.32,
                    hatch="//",
                    label="Selected spike mass (first bin)",
                )
        else:
            values, density = fit_pdf_on_grid(row)
            scaled_density = density * total_weight * 2.0
        (line,) = ax.plot(
            values,
            scaled_density,
            color=COLORS["selected"],
            linewidth=2.0,
            label=line_label,
            zorder=3,
        )
        selected_handles = [line]

        ax.text(
            0.025,
            0.965,
            f"{species}",
            transform=ax.transAxes,
            ha="left",
            va="top",
            fontsize=15,
            fontweight="bold",
        )
        ax.text(
            0.025,
            0.865,
            SPECIES_NAMES[species],
            transform=ax.transAxes,
            ha="left",
            va="top",
            fontsize=8,
            color=COLORS["muted"],
            style="italic",
        )

        short_label = SHORT_DISTRIBUTION_LABELS.get(
            str(row["distribution"]), str(row["distribution"])
        )
        if not bool(row.get("converged", True)):
            short_label = f"{short_label} (non-converged)"
        metadata = (
            f"{short_label}\n"
            f"n = {int(row['n_trees']):,} trees · {int(row['n_plots'])} plots\n"
            f"AIC {float(row['aic']):,.0f} · KS {float(row['ks']):.4f}"
        )
        ax.text(
            0.975,
            0.965,
            metadata,
            transform=ax.transAxes,
            ha="right",
            va="top",
            fontsize=7.4,
            linespacing=1.45,
        )
        style_panel(ax, xlabel=False, ylabel=species in {"AT", "PL"})
        ax.set_ylim(
            0.0,
            max(float(counts.max()), float(scaled_density.max()), float(spike_peak))
            * 1.18,
        )

    summary_ax = flat_axes[7]
    summary_ax.axis("off")
    summary_ax.text(
        0.0,
        0.97,
        "AU species composition",
        transform=summary_ax.transAxes,
        ha="left",
        va="top",
        fontsize=11,
        fontweight="bold",
    )
    summary_ax.text(
        0.0,
        0.90,
        "share of target TPH",
        transform=summary_ax.transAxes,
        ha="left",
        va="top",
        fontsize=8,
        color=COLORS["muted"],
    )
    header_y = 0.80
    summary_ax.text(
        0.0,
        header_y,
        "sp.",
        transform=summary_ax.transAxes,
        fontsize=7.2,
        color=COLORS["muted"],
        fontweight="bold",
    )
    summary_ax.text(
        0.16,
        header_y,
        "share",
        transform=summary_ax.transAxes,
        fontsize=7.2,
        color=COLORS["muted"],
        fontweight="bold",
    )
    summary_ax.text(
        0.40,
        header_y,
        "selected fit",
        transform=summary_ax.transAxes,
        fontsize=7.2,
        color=COLORS["muted"],
        fontweight="bold",
    )
    summary_ax.text(
        0.82,
        header_y,
        "KS",
        transform=summary_ax.transAxes,
        fontsize=7.2,
        color=COLORS["muted"],
        fontweight="bold",
    )
    summary_ax.plot(
        [0.0, 1.0],
        [header_y - 0.045, header_y - 0.045],
        color="#CBD5E1",
        linewidth=0.8,
        transform=summary_ax.transAxes,
        clip_on=False,
    )

    for index, species in enumerate(SPECIES_ORDER):
        row = au_fits[au_fits["species"] == species].iloc[0]
        y = 0.70 - index * 0.083
        summary_ax.text(
            0.0,
            y,
            species,
            transform=summary_ax.transAxes,
            fontsize=8.2,
            fontweight="bold",
            va="center",
        )
        summary_ax.text(
            0.16,
            y,
            f"{float(species_weights[species]):.1%}",
            transform=summary_ax.transAxes,
            fontsize=8.0,
            va="center",
        )
        summary_ax.text(
            0.40,
            y,
            SHORT_DISTRIBUTION_LABELS.get(str(row["distribution"]), str(row["distribution"])),
            transform=summary_ax.transAxes,
            fontsize=7.8,
            va="center",
        )
        summary_ax.text(
            0.82,
            y,
            f"{float(row['ks']):.3f}",
            transform=summary_ax.transAxes,
            fontsize=8.0,
            va="center",
        )

    summary_ax.text(
        0.0,
        0.035,
        "All selected fits are conditional on\nDBH ≥ 2 cm and age 80–120 yr.",
        transform=summary_ax.transAxes,
        fontsize=7.2,
        color=COLORS["muted"],
        va="bottom",
        linespacing=1.35,
    )

    fig.suptitle(
        "TSA24 Prince George · AU 23000 DBH distribution fits",
        x=0.5,
        y=0.995,
        fontsize=15,
        fontweight="bold",
    )
    fig.text(
        0.5,
        0.955,
        "Age 80–120 yr · Nechako Lowland (SBS) · selected fit per species · "
        f"spike-aware ({source_label} fits)",
        ha="center",
        va="top",
        fontsize=9.2,
        color=COLORS["muted"],
    )
    legend_handles = [
        Patch(
            facecolor=COLORS["observed_fill"],
            edgecolor=COLORS["observed_edge"],
            label="Observed PSP (expansion-weighted)",
        ),
        selected_handles[0],
    ]
    if spike_handle is not None:
        legend_handles.append(spike_handle)
    fig.legend(
        handles=legend_handles,
        loc="lower center",
        ncol=len(legend_handles),
        fontsize=8.5,
        bbox_to_anchor=(0.5, 0.002),
    )
    fig.text(
        0.985,
        0.012,
        f"Source: {source_label} distribution_fits.csv + FAIB PSP TSA24 live trees.",
        ha="right",
        va="bottom",
        fontsize=7.0,
        color="#6B7280",
    )
    fig.subplots_adjust(left=0.055, right=0.985, top=0.895, bottom=0.10, wspace=0.18, hspace=0.22)
    fig.savefig(output_path)
    plt.close(fig)


# ---------------------------------------------------------------------------
# Figure 2: CW high-KS strata
# ---------------------------------------------------------------------------


def plot_cw_high_ks(
    fits: pd.DataFrame,
    trees: pd.DataFrame,
    output_path: Path,
) -> None:
    expected_ids = tuple(
        f"{level}:{value}|CW" for level, value in CW_HIGH_KS_FITS
    )
    high_rows = fits[
        (fits["scope"] == "tsa24_all_ages")
        & (fits["fit_id"].isin(expected_ids))
        & (fits["selected"] == True)
    ].drop_duplicates("fit_id", keep="first")
    if high_rows.empty:
        raise ValueError("no CW diagnostic strata found in distribution_fits.csv")
    order = {fit_id: index for index, fit_id in enumerate(expected_ids)}
    high_rows = (
        high_rows.assign(_order=high_rows["fit_id"].map(order))
        .sort_values("_order")
        .drop(columns="_order")
        .reset_index(drop=True)
    )

    fig, axes = plt.subplots(1, 2, figsize=(13.6, 5.9), sharex=True)
    for ax, (_, selected_row) in zip(axes, high_rows.iterrows(), strict=True):
        fit_id = str(selected_row["fit_id"])
        fit_level = str(selected_row["fit_level"])
        level_value = fit_id.split(":", 1)[1].rsplit("|", 1)[0]
        subset = trees[
            trees["mapped"]
            & trees["species"].eq("CW")
            & trees[fit_level].astype(str).eq(level_value)
        ].copy()

        edges, counts = observed_counts(subset)
        centers = 0.5 * (edges[:-1] + edges[1:])
        observed_bars = ax.bar(
            centers,
            counts,
            width=1.82,
            align="center",
            color=COLORS["observed_fill"],
            edgecolor=COLORS["observed_edge"],
            linewidth=0.5,
            label="Observed PSP (expansion-weighted)",
            zorder=2,
        )
        ax.axvspan(2.0, 4.0, color="#F59E0B", alpha=0.10, zorder=0)
        ax.text(
            4.3,
            float(counts.max()) * 0.68,
            "first bin",
            fontsize=7.3,
            color="#92400E",
            va="top",
        )

        total_weight = float(subset["expansion_factor"].sum())
        curve_maxima: list[float] = []
        legend_handles: dict[str, Any] = {"observed": observed_bars}
        annotations = [
            (
                f"n = {int(selected_row['n_trees'])} trees · "
                f"{int(selected_row['n_plots'])} plots"
            )
        ]

        legacy = _fit_row_for(fits, fit_id, "mixture")
        if legacy is not None:
            values, density = fit_pdf_on_grid(legacy)
            scaled = density * total_weight * 2.0
            curve_maxima.append(float(np.nanmax(scaled)))
            (legacy_line,) = ax.plot(
                values,
                scaled,
                color=COLORS["candidate_gamma"],
                linestyle="--",
                linewidth=1.8,
                label=(
                    f"legacy two-gamma · AIC {float(legacy['aic']):,.0f} · "
                    f"KS {float(legacy['ks']):.3f}"
                ),
                zorder=3,
            )
            legend_handles["legacy"] = legacy_line
            annotations.append(
                f"{'two-gamma (legacy)':<26s} AIC {float(legacy['aic']):,.0f} · "
                f"KS {float(legacy['ks']):.4f}"
            )

        if str(selected_row["distribution"]) in SPIKE_COMPONENTS:
            values, density, spike_mass = spike_curve(selected_row)
            scaled = density * total_weight * 2.0
            curve_maxima.append(float(np.nanmax(scaled)))
            (selected_line,) = ax.plot(
                values,
                scaled,
                color=COLORS["selected"],
                linewidth=2.3,
                label=(
                    f"selected {SHORT_DISTRIBUTION_LABELS.get(str(selected_row['distribution']), str(selected_row['distribution']))} tail · "
                    f"AIC {float(selected_row['aic']):,.0f} · "
                    f"KS {float(selected_row['ks']):.3f}"
                ),
                zorder=4,
            )
            legend_handles["selected"] = selected_line
            width = float(spike_row_spec(selected_row)[1])
            spike_height = total_weight * spike_mass
            curve_maxima.append(spike_height)
            spike_bars = ax.bar(
                [float(selected_row["dbh_limit_cm"]) + width / 2.0],
                [spike_height],
                width=1.82,
                color=COLORS["selected"],
                alpha=0.32,
                edgecolor=COLORS["selected"],
                hatch="//",
                linewidth=0.6,
                label="selected spike first-bin mass",
                zorder=3,
            )
            legend_handles["spike"] = spike_bars
            annotations.insert(1, _spike_annotation(selected_row))
        else:
            values, density = fit_pdf_on_grid(selected_row)
            scaled = density * total_weight * 2.0
            curve_maxima.append(float(np.nanmax(scaled)))
            (selected_line,) = ax.plot(
                values,
                scaled,
                color=COLORS["selected"],
                linewidth=2.3,
                label=(
                    f"selected {SHORT_DISTRIBUTION_LABELS.get(str(selected_row['distribution']), str(selected_row['distribution']))} · "
                    f"AIC {float(selected_row['aic']):,.0f} · "
                    f"KS {float(selected_row['ks']):.3f}"
                ),
                zorder=4,
            )
            legend_handles["selected"] = selected_line
            annotations.insert(
                1,
                f"{selected_row['distribution']!s:<26s} "
                f"AIC {float(selected_row['aic']):,.0f} · "
                f"KS {float(selected_row['ks']):.4f}",
            )

        ax.text(
            0.025,
            0.975,
            f"{level_value}\n{fit_level} · CW",
            transform=ax.transAxes,
            ha="left",
            va="top",
            fontsize=10.5,
            fontweight="bold",
            linespacing=1.35,
        )
        ax.text(
            0.975,
            0.875,
            "\n".join(annotations),
            transform=ax.transAxes,
            ha="right",
            va="top",
            fontsize=6.6,
            family="DejaVu Sans Mono",
            linespacing=1.45,
            bbox={
                "boxstyle": "round,pad=0.4",
                "facecolor": "#F8FAFC",
                "edgecolor": "#CBD5E1",
                "linewidth": 0.7,
                "alpha": 0.94,
            },
            zorder=6,
        )
        ax.legend(
            handles=[
                legend_handles[key]
                for key in ("observed", "selected", "spike", "legacy")
                if key in legend_handles
            ],
            loc="upper right",
            bbox_to_anchor=(0.995, 0.71),
            fontsize=7.3,
            borderaxespad=0.4,
        )
        style_panel(ax, xlabel=True, ylabel=ax is axes[0])
        ax.set_ylim(
            0.0, max(float(counts.max()), max(curve_maxima, default=0.0)) * 1.16
        )

    fig.suptitle(
        "TSA24 · CW high-KS strata: first-bin-dominated DBH shape",
        x=0.5,
        y=0.995,
        fontsize=14,
        fontweight="bold",
    )
    fig.text(
        0.5,
        0.945,
        "Montane Cordillera / Columbia Montane Cordillera · all ages · "
        "selected legacy two-gamma and diagnostic Weibull mixtures",
        ha="center",
        va="top",
        fontsize=9,
        color=COLORS["muted"],
    )
    fig.text(
        0.5,
        0.012,
        "The observed first-bin atom drives the KS statistic. No finite-mean constrained spike "
        "passes the bound test here, so the legacy two-gamma remains selected; the Weibull "
        "mixtures stay as diagnostics.",
        ha="center",
        va="bottom",
        fontsize=7.8,
        color="#6B7280",
    )
    fig.subplots_adjust(left=0.06, right=0.985, top=0.865, bottom=0.15, wspace=0.16)
    fig.savefig(output_path)
    plt.close(fig)


# ---------------------------------------------------------------------------
# Figure 2b: CW constrained spike diagnostics
# ---------------------------------------------------------------------------


def _fit_row_for(
    fits: pd.DataFrame, fit_id: str, distribution: str
) -> pd.Series | None:
    rows = fits[
        (fits["scope"] == "tsa24_all_ages")
        & (fits["fit_id"] == fit_id)
        & (fits["distribution"] == distribution)
        & (fits["fit_status"].isin(["ok", "boundary_reject"]))
    ].drop_duplicates("distribution")
    return rows.iloc[0] if len(rows) else None


def _spike_annotation(row: pd.Series) -> str:
    weight, _width, component, parameters = spike_row_spec(row)
    shape_key = "a" if component == "weibull" else "p"
    distribution = str(row["distribution"])
    status = (
        "audit-only (infinite-mean tail)"
        if distribution in {"spike_weibull", "spike_gamma"}
        else spike_boundary_text(row)
    )
    return (
        f"{distribution:<26s} w {weight:.4f} · "
        f"{shape_key} {float(parameters[shape_key]):.4g} · "
        f"β {float(parameters['beta']):.4g} · "
        f"AIC {float(row['aic']):,.0f} · KS {float(row['ks']):.4f} · "
        f"{status}"
    )


def plot_cw_spike(
    fits: pd.DataFrame,
    trees: pd.DataFrame,
    output_path: Path,
) -> None:
    """Plot observed CW tallies, the legacy fit, and both constrained spikes."""
    fig, axes = plt.subplots(1, 2, figsize=(15.0, 6.8), sharex=True)
    spike_colors = {
        "spike_weibull_constrained": COLORS["accent"],
        "spike_gamma_constrained": COLORS["candidate_gamma"],
    }
    for ax, (level, value) in zip(axes, CW_HIGH_KS_FITS, strict=True):
        fit_id = f"{level}:{value}|CW"
        subset = trees[
            trees["mapped"]
            & trees["species"].eq("CW")
            & trees[level].astype(str).eq(value)
        ].copy()
        if subset.empty:
            raise ValueError(f"no CW trees for {fit_id}")
        selected_rows = fits[
            (fits["scope"] == "tsa24_all_ages")
            & (fits["fit_id"] == fit_id)
            & (fits["selected"] == True)
        ].drop_duplicates("fit_id")
        if selected_rows.empty:
            raise ValueError(f"no selected fit for {fit_id}")
        selected_row = selected_rows.iloc[0]

        edges, counts = observed_counts(subset)
        centers = 0.5 * (edges[:-1] + edges[1:])
        total = float(np.sum(counts))
        observed_bars = ax.bar(
            centers,
            counts,
            width=1.82,
            align="center",
            color=COLORS["observed_fill"],
            edgecolor=COLORS["observed_edge"],
            linewidth=0.5,
            label="Observed PSP (expansion-weighted)",
            zorder=2,
        )
        lower = float(selected_row["dbh_limit_cm"])
        first_upper = lower + 2.0
        ax.axvspan(lower, first_upper, color="#F59E0B", alpha=0.11, zorder=0)
        ax.text(
            first_upper + 0.4,
            float(counts.max()) * 0.94,
            "first bin",
            fontsize=7.5,
            color="#92400E",
            va="top",
        )

        curve_maxima = [float(counts.max())]
        legend_handles: dict[str, Any] = {"observed": observed_bars}
        legacy = _fit_row_for(fits, fit_id, "mixture")
        if legacy is not None:
            values, density = fit_pdf_on_grid(legacy)
            scaled = density * total * 2.0
            curve_maxima.append(float(np.nanmax(scaled)))
            (legacy_line,) = ax.plot(
                values,
                scaled,
                color=COLORS["candidate_gamma"],
                linestyle="--",
                linewidth=1.8,
                label=(
                    f"two-gamma legacy · AIC {float(legacy['aic']):,.0f} · "
                    f"KS {float(legacy['ks']):.3f}"
                ),
                zorder=3,
            )
            legend_handles["legacy"] = legacy_line

        annotations = [
            (
                f"n = {int(selected_row['n_trees'])} trees · "
                f"{int(selected_row['n_plots'])} plots · "
                f"first-bin share {counts[1] / total:.4f}"
            )
        ]
        if str(selected_row["distribution"]) in SPIKE_COMPONENTS:
            values, density, spike_mass = spike_curve(selected_row)
            scaled = density * total * 2.0
            curve_maxima.append(float(np.nanmax(scaled)))
            (selected_line,) = ax.plot(
                values,
                scaled,
                color=COLORS["selected"],
                linewidth=2.4,
                label=(
                    f"selected {DISTRIBUTION_LABELS.get(str(selected_row['distribution']), str(selected_row['distribution']))} tail · "
                    f"AIC {float(selected_row['aic']):,.0f} · "
                    f"KS {float(selected_row['ks']):.3f}"
                ),
                zorder=5,
            )
            legend_handles["selected"] = selected_line
            width = float(spike_row_spec(selected_row)[1])
            spike_height = total * spike_mass
            curve_maxima.append(spike_height)
            spike_bars = ax.bar(
                [lower + width / 2.0],
                [spike_height],
                width=1.82,
                color=COLORS["selected"],
                alpha=0.35,
                edgecolor=COLORS["selected"],
                hatch="//",
                linewidth=0.6,
                label="selected spike first-bin mass",
                zorder=5,
            )
            legend_handles["spike"] = spike_bars
            annotations.append(_spike_annotation(selected_row))
        else:
            values, density = fit_pdf_on_grid(selected_row)
            scaled = density * total * 2.0
            curve_maxima.append(float(np.nanmax(scaled)))
            (selected_line,) = ax.plot(
                values,
                scaled,
                color=COLORS["selected"],
                linewidth=2.4,
                label=(
                    f"selected {DISTRIBUTION_LABELS.get(str(selected_row['distribution']), str(selected_row['distribution']))} · "
                    f"AIC {float(selected_row['aic']):,.0f} · "
                    f"KS {float(selected_row['ks']):.3f}"
                ),
                zorder=5,
            )
            legend_handles["selected"] = selected_line
        if legacy is not None:
            annotations.append(
                f"{'two-gamma (legacy)':<26s} AIC {float(legacy['aic']):,.0f} · "
                f"KS {float(legacy['ks']):.4f}"
            )
        unconstrained = _fit_row_for(fits, fit_id, "spike_weibull")
        if (
            unconstrained is not None
            and str(selected_row["distribution"]) != "spike_weibull"
        ):
            values, density, spike_mass = spike_curve(unconstrained)
            scaled = density * total * 2.0
            curve_maxima.append(float(np.nanmax(scaled)))
            (audit_line,) = ax.plot(
                values,
                scaled,
                color=COLORS["ink"],
                linestyle=":",
                linewidth=1.6,
                label=(
                    f"spike_weibull audit · AIC {float(unconstrained['aic']):,.0f} · "
                    f"KS {float(unconstrained['ks']):.3f}"
                ),
                zorder=4,
            )
            legend_handles["audit"] = audit_line
            width = float(spike_row_spec(unconstrained)[1])
            spike_height = total * spike_mass
            curve_maxima.append(spike_height)
            ax.bar(
                [lower + width / 2.0],
                [spike_height],
                width=1.82,
                color=COLORS["ink"],
                alpha=0.18,
                edgecolor=COLORS["ink"],
                linewidth=0.5,
                zorder=4,
            )
            annotations.append(_spike_annotation(unconstrained))

        for distribution in (
            "spike_weibull_constrained",
            "spike_gamma_constrained",
        ):
            row = _fit_row_for(fits, fit_id, distribution)
            if row is None:
                continue
            values, density, spike_mass = spike_curve(row)
            scaled = density * total * 2.0
            curve_maxima.append(float(np.nanmax(scaled)))
            color = spike_colors[distribution]
            (constrained_line,) = ax.plot(
                values,
                scaled,
                color=color,
                linewidth=1.9,
                linestyle="-",
                label=(
                    f"{DISTRIBUTION_LABELS[distribution]} tail · "
                    f"AIC {float(row['aic']):,.0f} · KS {float(row['ks']):.3f}"
                ),
                zorder=3,
            )
            legend_handles[distribution] = constrained_line
            width = float(spike_row_spec(row)[1])
            ax.bar(
                [lower + width / 2.0],
                [total * spike_mass],
                width=1.82,
                color=color,
                alpha=0.25,
                edgecolor=color,
                hatch="//",
                linewidth=0.6,
                label=f"{DISTRIBUTION_LABELS[distribution]} first-bin mass",
                zorder=3,
            )
            annotations.append(_spike_annotation(row))

        ax.text(
            0.025,
            0.975,
            f"{value}\n{level} · CW",
            transform=ax.transAxes,
            ha="left",
            va="top",
            fontsize=10.5,
            fontweight="bold",
            linespacing=1.35,
        )
        ax.text(
            0.975,
            0.79,
            "\n".join(annotations),
            transform=ax.transAxes,
            ha="right",
            va="top",
            fontsize=6.6,
            family="DejaVu Sans Mono",
            linespacing=1.45,
            bbox={
                "boxstyle": "round,pad=0.4",
                "facecolor": "#F8FAFC",
                "edgecolor": "#CBD5E1",
                "linewidth": 0.7,
                "alpha": 0.95,
            },
            zorder=6,
        )
        ax.legend(
            handles=[
                legend_handles[key]
                for key in (
                    "observed",
                    "selected",
                    "spike",
                    "legacy",
                    "spike_weibull_constrained",
                    "spike_gamma_constrained",
                    "audit",
                )
                if key in legend_handles
            ],
            loc="upper right",
            bbox_to_anchor=(0.995, 0.53),
            fontsize=7.0,
            borderaxespad=0.4,
        )
        style_panel(ax, xlabel=True, ylabel=ax is axes[0])
        ax.set_ylim(0.0, max(curve_maxima) * 1.18)

    fig.suptitle(
        "TSA24 · CW spike re-fit: constrained finite-mean tails vs legacy and audit fits",
        x=0.5,
        y=0.995,
        fontsize=14,
        fontweight="bold",
    )
    fig.text(
        0.5,
        0.945,
        "Observed tallies, selected legacy two-gamma, constrained grouped-MLE spike alternatives, "
        "and unconstrained audit · shape ≥ 1, scale ≥ 0.1 cm",
        ha="center",
        va="top",
        fontsize=9.2,
        color=COLORS["muted"],
    )
    fig.text(
        0.5,
        0.012,
        "Constrained Weibull/gamma tails hit the a=1 / p=1 finite-mean boundary and are marked "
        "boundary_reject. The legacy finite-mean two-gamma remains selected; the unconstrained "
        "spike is audit-only and not synthesis-eligible because its untruncated mean is infinite.",
        ha="center",
        va="bottom",
        fontsize=7.6,
        color="#6B7280",
    )
    fig.subplots_adjust(left=0.055, right=0.985, top=0.86, bottom=0.15, wspace=0.12)
    fig.savefig(output_path)
    plt.close(fig)


# ---------------------------------------------------------------------------
# Figure 3: synthetic tree DBH
# ---------------------------------------------------------------------------


def plot_synthetic_dbh(
    synthetic: pd.DataFrame,
    target_stand: Mapping[str, Any],
    output_path: Path,
    *,
    source_label: str = "working-tree",
) -> None:
    edges = np.arange(0.0, 82.0, 2.0)
    counts, _ = np.histogram(
        synthetic["dbh_cm"].to_numpy(dtype=float),
        bins=edges,
        weights=synthetic["tph"].to_numpy(dtype=float),
    )
    centers = 0.5 * (edges[:-1] + edges[1:])

    tph = float(synthetic["tph"].sum())
    ba = float(synthetic["stem_basal_area_m2ha"].sum())
    volume = float(synthetic["taper_volume_m3ha"].sum())
    qmd = 100.0 * math.sqrt(4.0 * ba / (math.pi * tph))
    target_tph = float(target_stand["tph_total"])
    target_volume = float(target_stand["volume_m3ha"])

    fig, ax = plt.subplots(figsize=(10.8, 6.2))
    ax.bar(
        centers,
        counts,
        width=1.82,
        align="center",
        color="#2F6F8F",
        edgecolor="#1E4E66",
        linewidth=0.5,
        zorder=2,
    )
    ax.axvline(
        qmd,
        color=COLORS["selected"],
        linestyle="--",
        linewidth=1.6,
        label=f"Synthetic QMD {qmd:.1f} cm",
        zorder=3,
    )
    stat_rows = (
        ("Target TPH", f"{target_tph:,.1f} ha⁻¹"),
        ("Synthetic TPH", f"{tph:,.1f} ha⁻¹"),
        ("Synthetic QMD", f"{qmd:.2f} cm"),
        ("Synthetic BA", f"{ba:.2f} m² ha⁻¹"),
        ("Target volume", f"{target_volume:.1f} m³ ha⁻¹"),
        ("Synthetic volume", f"{volume:.1f} m³ ha⁻¹"),
        ("Trees", f"{len(synthetic):,}"),
    )
    stat_text = "\n".join(f"{label:<16}{value:>21}" for label, value in stat_rows)
    ax.text(
        0.975,
        0.965,
        stat_text,
        transform=ax.transAxes,
        ha="right",
        va="top",
        fontsize=8.5,
        family="DejaVu Sans Mono",
        linespacing=1.55,
        bbox={
            "boxstyle": "round,pad=0.55",
            "facecolor": "#F8FAFC",
            "edgecolor": "#CBD5E1",
            "linewidth": 0.8,
        },
        zorder=5,
    )

    style_panel(ax, xlabel=True, ylabel=True)
    ax.set_ylim(0.0, float(counts.max()) * 1.18)
    ax.set_title(
        f"Synthetic tree DBH distribution · TSA24 AU {int(target_stand['au_id']):,}, "
        f"age {float(target_stand['age']):.0f}",
        loc="left",
        pad=14,
    )
    ax.text(
        0.0,
        1.015,
        f"{len(synthetic):,} trees drawn from the selected AU species distributions; "
        f"TPH- and volume-constrained to {target_tph:,.0f} ha⁻¹ and "
        f"{target_volume:.1f} m³/ha.",
        transform=ax.transAxes,
        ha="left",
        va="bottom",
        fontsize=8.6,
        color=COLORS["muted"],
    )
    ax.legend(loc="upper left", fontsize=8.2, bbox_to_anchor=(0.0, 0.93))
    fig.text(
        0.985,
        0.012,
        f"Source: {source_label} synthetic_trees.csv and target_stand.json.",
        ha="right",
        va="bottom",
        fontsize=7.0,
        color="#6B7280",
    )
    fig.subplots_adjust(left=0.09, right=0.985, top=0.86, bottom=0.12)
    fig.savefig(output_path)
    plt.close(fig)


# ---------------------------------------------------------------------------
# Figure 4: assortment matrix
# ---------------------------------------------------------------------------


def plot_assortment(
    matrix: pd.DataFrame,
    residue_ledger: pd.DataFrame,
    synthetic: pd.DataFrame,
    target_stand: Mapping[str, Any],
    output_path: Path,
    *,
    source_label: str = "working-tree",
) -> None:
    product_order = ("sawlog", "pulpwood", "other", "residue")
    product_colors = {
        "sawlog": COLORS["sawlog"],
        "pulpwood": COLORS["pulpwood"],
        "other": COLORS["other"],
        "residue": COLORS["residue"],
    }
    log_and_residue = matrix[matrix["record_type"] != "total"].copy()
    pivot = (
        log_and_residue.pivot_table(
            index="species",
            columns="product",
            values="volume_m3",
            aggfunc="sum",
            fill_value=0.0,
        )
        .reindex(columns=list(product_order), fill_value=0.0)
        .reindex(SPECIES_ORDER)
        .fillna(0.0)
    )
    pivot = pivot.loc[pivot.sum(axis=1).sort_values(ascending=False).index]

    stand_total = float(
        matrix.loc[
            matrix["is_total"].astype(str).str.lower().eq("true"), "volume_m3"
        ].sum()
    )
    if not math.isclose(float(pivot.to_numpy().sum()), stand_total, rel_tol=1.0e-9):
        raise ValueError(
            f"species/product volumes sum to {pivot.to_numpy().sum():.3f}, "
            f"not the matrix total {stand_total:.3f}"
        )

    ledger_scaled = residue_ledger.merge(
        synthetic[["tree_id", "tph"]], on="tree_id", how="left", validate="one_to_one"
    )
    if ledger_scaled["tph"].isna().any():
        raise ValueError("residue ledger tree IDs did not all match synthetic_trees.csv")
    ledger_residue_m3ha = float(
        (ledger_scaled["residue_volume_m3"] * ledger_scaled["tph"]).sum()
    )
    matrix_residue_m3ha = float(pivot["residue"].sum())

    fig, ax = plt.subplots(figsize=(11.6, 6.2))
    x = np.arange(len(pivot))
    bottom = np.zeros(len(pivot), dtype=float)
    for product in product_order:
        values = pivot[product].to_numpy(dtype=float)
        ax.bar(
            x,
            values,
            bottom=bottom,
            width=0.66,
            color=product_colors[product],
            edgecolor="white",
            linewidth=0.7,
            label=product,
            zorder=2,
        )
        bottom += values

    for index, total in enumerate(bottom):
        ax.text(
            index,
            total + stand_total * 0.012,
            f"{total:.1f}",
            ha="center",
            va="bottom",
            fontsize=8.2,
            fontweight="bold",
        )

    ax.axhline(
        stand_total,
        color=COLORS["selected"],
        linestyle="--",
        linewidth=1.1,
        zorder=1,
        label=f"Stand total {stand_total:.1f} m³/ha",
    )
    ax.set_xticks(x)
    ax.set_xticklabels(
        [f"{species}\n{SPECIES_NAMES[species]}" for species in pivot.index],
        fontsize=8.2,
        linespacing=1.35,
    )
    ax.set_ylim(0.0, stand_total * 1.16)
    style_panel(ax, xlabel=False, ylabel=False)
    ax.set_ylabel("Recovered volume (m$^3$ ha$^{-1}$)")
    ax.set_xlim(-0.6, len(pivot) - 0.4)
    ax.grid(axis="x", visible=False)

    ax.set_title(
        f"Assortment recovery by species and product · TSA24 AU "
        f"{int(target_stand['au_id']):,}, age {float(target_stand['age']):.0f}",
        loc="left",
        pad=14,
    )
    ax.text(
        0.0,
        1.015,
        "Sawlog + pulpwood + other + residue; TPH- and volume-constrained 1 ha "
        "target stand; residue is the taper-balance residual.",
        transform=ax.transAxes,
        ha="left",
        va="bottom",
        fontsize=8.6,
        color=COLORS["muted"],
    )
    handles, labels = ax.get_legend_handles_labels()
    ax.legend(
        handles,
        labels,
        loc="upper right",
        ncol=2,
        fontsize=8.2,
        borderaxespad=0.6,
    )
    ax.text(
        0.985,
        0.45,
        f"Matrix residue  {matrix_residue_m3ha:.2f} m³/ha\n"
        f"Ledger cross-check {ledger_residue_m3ha:.2f} m³/ha\n"
        f"Difference       {abs(matrix_residue_m3ha - ledger_residue_m3ha):.2f} m³/ha",
        transform=ax.transAxes,
        ha="right",
        va="top",
        fontsize=7.6,
        family="DejaVu Sans Mono",
        linespacing=1.45,
        bbox={
            "boxstyle": "round,pad=0.45",
            "facecolor": "#F8FAFC",
            "edgecolor": "#CBD5E1",
            "linewidth": 0.7,
        },
    )
    fig.text(
        0.985,
        0.012,
        f"Source: {source_label} assortment_matrix.csv, residue_ledger.csv, and synthetic_trees.csv.",
        ha="right",
        va="bottom",
        fontsize=7.0,
        color="#6B7280",
    )
    fig.subplots_adjust(left=0.085, right=0.985, top=0.86, bottom=0.15)
    fig.savefig(output_path)
    plt.close(fig)


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument(
        "--working",
        dest="working",
        action="store_true",
        default=True,
        help="read the working-tree prototype CSVs/JSON (default)",
    )
    mode.add_argument(
        "--committed",
        dest="working",
        action="store_false",
        help="read the committed HEAD snapshots instead of the working tree",
    )
    args = parser.parse_args(argv)
    working = bool(args.working)
    source_label = "working-tree" if working else "committed HEAD"

    fits = read_csv_artifact(DATA_ROOT, "distribution_fits.csv", working=working)
    target_stand = read_json_artifact(DATA_ROOT, "target_stand.json", working=working)
    synthetic = read_csv_artifact(DATA_ROOT, "synthetic_trees.csv", working=working)
    matrix = read_csv_artifact(DATA_ROOT, "assortment_matrix.csv", working=working)
    residue_ledger = read_csv_artifact(
        DATA_ROOT, "residue_ledger.csv", working=working
    )

    trees = load_observed_trees(REPO_ROOT, DATA_ROOT, working=working)

    plot_au_fits(
        fits,
        trees,
        target_stand,
        PLOT_DIR / "tsa24_dbh_fits.png",
        source_label=source_label,
    )
    plot_cw_high_ks(
        fits,
        trees,
        PLOT_DIR / "tsa24_cw_high_ks.png",
    )
    plot_cw_spike(
        fits,
        trees,
        PLOT_DIR / "tsa24_cw_spike.png",
    )
    plot_synthetic_dbh(
        synthetic,
        target_stand,
        PLOT_DIR / "tsa24_synthetic_dbh.png",
        source_label=source_label,
    )
    plot_assortment(
        matrix,
        residue_ledger,
        synthetic,
        target_stand,
        PLOT_DIR / "tsa24_assortment.png",
        source_label=source_label,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
