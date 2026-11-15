# TSA24 grade and residue curves

Status: compiled from refreshed TSA24 BTC `/TSR` output (log-grades and
residual-fibre indicator banks). Model output, not field grade.
Generated: 2026-11-15.

This note records how the TSA24 grade/residue benchmark was produced, what it
covers, and what it does not cover. The pilot report and
`grade_benchmark_summary.json` carry the numeric comparison.

## 1. Grade path decision

The benchmark path is the documented FEMIC BTC path:

```bash
python -m femic tipsy run-btc data/03_input-tsa24.csv \
  --indicator-bank log-grades --indicator-bank residual-fibre \
  --run-id tsa24_grades

python -m femic tsa btc-post-tipsy \
  --instance-root /srv/shared-data/gep/ws4/femic/external/femic-tsa24-instance \
  --run-config config/run_profile.tsa24.yaml --tsa 24 --run-id tsa24_grades \
  --indicator-bank log-grades --indicator-bank residual-fibre
```

The local wrapper is:

```sh
#!/bin/sh
exec xvfb-run -a wine "$(dirname "$0")/TIPSYbtc_real.exe" "$@"
```

The Linux host needed `wine` and `xvfb` plus Wine Mono:

```bash
sudo apt-get update
sudo apt-get install -y wine xvfb
xvfb-run -a wine msiexec /i wine-mono-9.0.0-x86.msi /qn
```

A bounded `/TSR` smoke against `Samples/ex1.csv` completed with exit code 0 and
wrote the expected output and error CSVs. The full TSA24 run completed with
exit code 0 and an empty `04_error-tsa24.csv` (header only).

The previous nominal-site-index `.taf` compile is superseded. It is retained
only in git history and in `tsa24_grade_curves.py` as historical context.

## 2. Compile

```bash
.venv/bin/python -m workflows.national.bucking.compile_tsa24_grade_curves \
  --femic-root /srv/shared-data/gep/ws4/femic/external/femic-tsa24-instance \
  --out-dir data/derived/national/bucking/tsa24_grade_curves
```

The compile reads `data/tipsy_curves_tsa24.csv`, which FEMIC derives from
`data/04_output-tsa24.csv`. It does not read the TIPSY `.taf` database and does
not apply a nominal site index, species surrogate, or grade-share rescale.

## 3. Coverage

- AUs: **16** of 16 TSA24 managed-curve AUs in `03_input-tsa24.csv`.
- Ages: **36** per AU (0–350 by 10 years); **576** AU-age rows.
- Grades: `Logs_Grade_D/F/H/I/J/U/X/Y`.
- Residual fibre: `Residual_Chips/Sawdust/Shavings/Trim/Bark`.
- `Logs_Grade_D` and `Logs_Grade_F` are zero for every AU in this run.
- `DBHq` and `TPH` are absent because the stand-structure bank was not
  requested.
- Industrial sort columns are absent because the industrial-logs bank was not
  requested.

| au_id | stratum_code | si_level | bec_zone | leading_species | au_site_index | planted_density_tph | grade_coverage_mean | zero_grade_columns |
|---|---|---|---|---|---|---|---|---|
| 21002 | SBS_PLI | L | SBS | PLI | 12.9 | 1700.0 | 1.116 | D,F |
| 21007 | SBS_SX+AT | L | SBS | SX | 13.7 | 1600.0 | 1.063 | D,F |
| 21008 | SBS_FDI | L | SBS | FDI | 15.7 | 1600.0 | 1.155 | D,F |
| 22000 | SBS_SX | M | SBS | SX | 13.8 | 1600.0 | 1.064 | D,F |
| 22002 | SBS_PLI | M | SBS | PLI | 15.5 | 1700.0 | 1.015 | D,F |
| 22003 | SBS_BL | M | SBS | BL | 12.7 | 2500.0 | 1.222 | D,F |
| 22004 | ESSF_SE | M | ESSF | SE | 10.5 | 1500.0 | 1.281 | D,F |
| 22007 | SBS_SX+AT | M | SBS | SX | 16.8 | 1600.0 | 1.067 | D,F |
| 22008 | SBS_FDI | M | SBS | FDI | 18.0 | 1600.0 | 1.178 | D,F |
| 23000 | SBS_SX | H | SBS | SX | 17.9 | 1600.0 | 1.039 | D,F |
| 23001 | ESSF_BL | H | ESSF | BL | 11.1 | 1500.0 | 1.128 | D,F |
| 23002 | SBS_PLI | H | SBS | PLI | 19.0 | 1700.0 | 1.009 | D,F |
| 23003 | SBS_BL | H | SBS | BL | 16.8 | 2500.0 | 1.082 | D,F |
| 23004 | ESSF_SE | H | ESSF | SE | 13.1 | 1500.0 | 1.139 | D,F |
| 23007 | SBS_SX+AT | H | SBS | SX | 21.3 | 1600.0 | 0.991 | D,F |
| 23008 | SBS_FDI | H | SBS | FDI | 20.6 | 1600.0 | 1.098 | D,F |

`bec_zone`, `stratum_code`, and `si_level` come from the AU crosswalk
(`au_table.csv` + `03_input`). The AU stratum code is the authority for the
BEC/species identity; this avoids the earlier mismatch where an input opening
BEC (for example ICH) disagreed with the attached untreated stratum (SBS_SX).

## 4. Output columns

`managed_au_curves.csv` (576 rows):

| Group | Columns |
|---|---|
| Keys | `au_id`, `au_table_au_id`, `managed_curve_id`, `stratum_code`, `si_level`, `leading_species`, `age` |
| Base curve | `volume`, `height`, `dbhq`, `tph`, `gross_yield`, `crown_cover` |
| Grades (m³/ha) | `Logs_Grade_D/F/H/I/J/U/X/Y` |
| Residual fibre (ODT/ha) | `Residual_Chips`, `Residual_Sawdust`, `Residual_Shavings`, `Residual_Trim`, `Residual_Bark` |
| Accounting | `grade_total_m3ha`, `grade_coverage_fraction`, `residual_fibre_odt_ha`, `residue_odt_per_m3`, `age_extrapolated`, `source` |

`managed_au_industrial_sorts.csv` is header-only in this pass because the
industrial-logs bank was not requested. It is retained so the benchmark can
distinguish "not requested" from "missing file".

`species_grade_curves.csv` carries same-species mean curves for pilot plots
that have no managed AU curve. It is a fallback surface, not an AU assignment.

`au_grade_coverage.csv` records the AU crosswalk, site index, planted density,
grade coverage, and zero-grade columns.

## 5. Transformations and limitations

- **No grade rescale.** Grade and residue values are direct BTC `/TSR` output
  at the AU and age. Grade totals can exceed `volume` at young ages and in
  mixed stands because `MVcon_*` is conifer merchantable volume while
  `Logs_Grade_*` covers the full graded log output. `grade_coverage_fraction`
  records the ratio rather than hiding it.
- **D/F zero.** `Logs_Grade_D` and `Logs_Grade_F` are zero for every TSA24 AU
  and age in this run. The benchmark therefore covers the H/I/J/U/X/Y surface.
  This is a BTC model result for these stand types and product rules, not a
  missing-column failure.
- **Residual fibre is mill residue.** BTC `Residual_Chips`, `Sawdust`,
  `Shavings`, `Trim`, and `Bark` are processing residues. The pilot residue is
  harvest slash (`taper total - recovered logs`). The two are reported side by
  side but are not equivalent.
- **No industrial sorts.** The industrial-logs bank was not requested, so the
  industrial-sort share comparison is marked unavailable rather than reusing
  the old nominal-SI table.
- **Model output, not field grade.** `Logs_Grade_*` is TIPSY/SYLVER model
  output. It is not an official BC scale grade and carries no defect, sweep,
  knot, or rot observation.

## 6. Provenance

| Item | SHA-256 |
|---|---|
| `03_input-tsa24.csv` | `e3c518bdad74a7b7897d44da6d36d93f513bcbfc29495123a7a91b5b24566042` |
| `04_output-tsa24.csv` | `0b7d020b91e118fce4cc67d2d50680e33fa48afe0b429c0413226d846e1d69f9` |
| `tipsy_curves_tsa24.csv` | `ccb7bb0ead30381c355646b3b1f1cb7668537b3f7dbe4d8e237c963df1ed540a` |
| `au_table.csv` | `fbaeb44b241e73373dfa0cf9b730cafed0f3e6f15f944056d35268d4b06b3099` |
| BTC manifest | `d4a659b391b5b153de5b8af3f0772a8c84c029fd7f5a0dc604c3cd0c26d59587` |
| `TIPSYbtc.exe` wrapper | `5491f2047407c7a645673906515f64f152c59578f1ea4a54b3194ab40c933426` |
| `TIPSYbtc_real.exe` | `17a5f35533b1c367df4ee1ff6f52c269b561d5ea4014cf1b592b8b3c24fb72da` |

Source model: TIPSY 4.7 BTC `/TSR`, Ministry Standard Database, February 2022.
Output hashes are in `data/derived/national/bucking/tsa24_grade_curves/manifest.json`.

## 7. Validation join

`validate_tsa24.py` maps each pilot plot to a TSA24 managed AU using the FEMIC
AU crosswalk:

```text
FAIB plot
  -> BEC + leading species -> managed AU stratum (including SBS_SX+AT)
  -> FEMIC AU site-index class -> L/M/H
  -> managed source AU in au_table -> BTC /TSR curve AU
  -> interpolate BTC curve at FAIB stand age
```

Plots without a managed AU curve use a same-species mean of the managed curves
and are labelled `species_curve`. Plots with no supported species or no stand
age are labelled `no_match` and excluded from share metrics.

The comparison is reported as:

- TIPSY `Logs_Grade_*` shares as a proxy only, because the pilot has
  `grade_status=not_assigned`;
- residue ODT/ha and ODT/m³ with the mill-vs-harvest caveat;
- no industrial-sort comparison in this pass (no industrial-logs bank);
- no value comparison, because no same-basis interior grade price vector is
  available.
