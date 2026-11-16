# TSA24 DBH fit diagnostics

These figures show the constrained-spike TSA24 DBH distribution fits.  They
are generated from the working-tree CSVs with `--working`, so they always match
the artifacts in the parent directory.  The default (no flag) still reads a
read-only `git show HEAD:...` snapshot for reproducible historical figures.

## Files

| File | Description |
| --- | --- |
| `tsa24_dbh_fits.png` | 2×4 panel grid: observed expansion-weighted DBH histogram and selected fitted PDF for each AU species (AT, BL, EP, FD, PL, SB, SW). The eighth panel summarises species shares, selected families, and KS. A selected spike model is drawn as a first-bin mass plus its conditional tail. |
| `tsa24_cw_high_ks.png` | CW diagnostic strata (Montane Cordillera ecozone and Columbia Montane Cordillera ecoprovince). Observed histograms, the selected legacy two-gamma fit, and diagnostic 2-Weibull and Weibull+gamma candidates are overlaid; the 2–4 cm first bin is shaded. |
| `tsa24_cw_spike.png` | CW constrained-spike diagnosis. Observed tallies, the legacy selected mixture, the constrained `spike_weibull` and `spike_gamma` tails and first-bin masses. The annotation reports weight, shape, scale, AIC, KS, and whether the constrained tail sits on a bound. The unconstrained spike is shown as an audit line in the annotation (infinite-mean tail, not selected). |
| `tsa24_synthetic_dbh.png` | Expansion-weighted DBH histogram of the 600 synthetic trees, with target/achieved TPH, synthetic QMD/basal area, and target/achieved volume annotations. The tree list is constrained to both targets. |
| `tsa24_assortment.png` | Stacked assortment volume by species × product (sawlog, pulpwood, other, residue), with the stand total and a residue-ledger cross-check. |

`make_plots.py --working` regenerates all five figures from the working-tree
artifacts.

## Method

- With `--working`, CSV/JSON artifacts are read directly from
  `data/derived/national/assortments/tsa24_prototype/`.  Without the flag,
  artifacts come from `git -C data show HEAD:derived/national/assortments/tsa24_prototype/<file>`.
- Observed histograms use the TSA24 FAIB PSP live-tree subset loaded through
  the working-tree (or HEAD, without the flag) `validate_tsa24.load_tsa24_data`
  code: TSA “Prince George”, mapped plots, species, ecodistrict, and the AU age
  window (80–120 yr). Bar heights are expansion-weighted
  (`expansion_factor`), so the vertical axis is trees per hectare per 2 cm bin.
  `dbh_validation.csv` stores quantiles rather than bin counts, so the
  histograms come from the raw trees.
- The AU fits are the rows in `distribution_fits.csv` with
  `scope = tsa24_au_age_window` and `selected = True`.  PDFs are reconstructed
  with SciPy: Weibull components use `weibull_min(a, scale=beta)`, gamma
  components use `gamma(p, scale=beta)`. Mixtures are weighted sums conditioned
  on the plot DBH limit (`dbh_limit_cm`), matching the reported KS convention.
- Spike rows are reconstructed with `spike_row_spec` / `spike_curve`: the
  continuous tail is conditioned on `DBH >= dbh_limit + spike_bin_width`, and
  the first-bin mass is drawn as a separate bar of height
  `spike_weight × total tally`.  The spike is not a density and is never drawn
  as a PDF spike at a point.
- The CW spike panel reads both the unconstrained audit rows and the
  constrained rows.  Boundary status comes from `spike_boundary_status` /
  `spike_at_bound`, falling back to the `fit_diagnostics` JSON for older CSVs.
- The synthetic panel uses per-tree TPH as the histogram weight. QMD is
  `100 × sqrt(4 × BA / (π × TPH))` with BA in m²/ha and TPH in trees/ha.
- The assortment panel aggregates `volume_m3` from non-total matrix rows.
  Residue from `residue_ledger.csv` is scaled by the matching synthetic-tree TPH
  and compared with the matrix residue total.

## Caveats

- The AT AU fit selected the legacy two-gamma `mixture` despite a non-converged
  EM (`converged = False`); it is annotated as a fallback in the figure.
- `target_stand.json` provides target TPH and volume, but not target QMD or
  basal area; the synthetic panel therefore labels QMD/BA as synthetic-stand
  metrics.
- The two CW diagnostic strata are first-bin dominated.  The constrained
  finite-mean Weibull/gamma tails are worse than the legacy two-gamma mixture
  in AIC and land on the shape bound; they are marked `boundary_reject` and are
  not selected.  The panel makes that restriction visible rather than hiding
  it.
- A smooth truncated Weibull sample can also be represented by a constrained
  spike within about three AIC units; the distribution table keeps the simple
  Weibull candidate for audit.

## Regenerate

From the repository root:

```bash
NEMORA_ROOT=/srv/shared-data/gep/ws4/nemora \
  .venv/bin/python data/derived/national/assortments/tsa24_prototype/plots/make_plots.py --working
```

The script requires `git`, `numpy`, `pandas`, `scipy`, `matplotlib`, and a
`nemora` checkout containing `src/nemora`. It writes only to this directory.
