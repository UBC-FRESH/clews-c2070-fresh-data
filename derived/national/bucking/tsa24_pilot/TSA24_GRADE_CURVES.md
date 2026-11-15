# TSA24 grade and residue curves

Status: compiled from TIPSY 4.5 `.taf` tables; model output, not field grade.
Generated: 2026-11-15.

This note records how the TSA24 grade/residue benchmark was produced, what it
covers, and what it does not cover.  The pilot report and
`grade_benchmark_summary.json` carry the numeric comparison.

## 1. Grade path decision

Two paths were checked.

### BTC (`femic tipsy run-btc`)

The CLI is present and starts, but unattended BTC is not usable on this host.
The local `TIPSYbtc.exe` is a POSIX wrapper:

```sh
#!/bin/sh
exec xvfb-run -a wine "$(dirname "$0")/TIPSYbtc_real.exe" "$@"
```

Neither `wine` nor `xvfb-run` is installed:

```text
$ command -v wine
$ command -v xvfb-run
```

A bounded probe against `data/03_input-tsa24.csv` failed closed:

```text
femic tipsy run-btc data/03_input-tsa24.csv \
  --btc-exe .../btc_install_wine/TIPSYbtc.exe \
  --use-installed-btc --run-id tsa24_btc_probe ...
```

```text
.../TIPSYbtc.exe: 2: exec: xvfb-run: not found
exit_code=127
RuntimeError: BTC did not create expected output file ...
```

No grade numbers were fabricated from the BTC path.  The probe manifest is
under the local run scratch area and is not a valid output.

### fresh-tipsy `.taf` (used)

The local TIPSY database has 96 `.tab`/`.taf` pairs.  `fresh-tipsy` parses the
151-field `.taf` surface directly, including:

- `Logs_Grade_D/F/H/I/J/U/X/Y` (m³/ha);
- `Residual_Chips/Sawdust/Shavings/Trim/Bark` (ODT/ha);
- 20 `Industrial_Logs_*` dimension sorts (m³/ha);
- diameter-class volume, biomass, and mortality fields.

This path needs no Windows runtime.  The parser and column map are from
`fresh-tipsy` (`fresh_tipsy.tables.parsers.parse_taf_file` and
`tab-taf-columns.csv`), not a hand-written field guess.

Exact compile command:

```bash
.venv/bin/python -m workflows.national.bucking.compile_tsa24_grade_curves \
  --femic-root "$FEMIC_TSA24_ROOT" \
  --tipsy-database "$TIPSY_DATABASE" \
  --out-dir data/derived/national/bucking/tsa24_grade_curves
```

## 2. Table and run selection

For each TSA24 `feature_id` in `data/03_input-tsa24.csv`:

1. Read the leading planted species and total planted density.
2. Resolve the species to a TIPSY `.taf` table.
3. Select the untreated (`pct_density=0`, `ct_density=0`) run block whose
   establishment density is closest to the AU density.
4. Interpolate all grade, residue, and industrial-sort columns to the standard
   FEMIC age grid (0–350 by 10 years).
5. Rescale grade volumes to the FEMIC managed merchantable volume (`Yield`) and
   scale residual fibre by `FEMIC volume / TAF Volume_Diameter_Class` sum.

Species mapping:

| TSA24 species | TIPSY table | Nominal SI | Basis |
|---|---|---:|---|
| `SW` | `sw 0530P00` | 20 | direct |
| `SE` | `sw 0530P00` | 20 | interior volume surrogate (`vriSpecies.txt` I-VOL=SW) |
| `BL` | `sw 0530P00` | 20 | interior volume surrogate (`vriSpecies.txt` I-VOL=SW) |
| `PL` | `pli0530P00` | 23 | direct |
| `FDI` | `fdi0535P00` | 25 | direct |
| `AT` | `at 1032P00` | 0 | direct; nominal SI not populated |
| `CW` | `cw 1040P00` | 0 | direct; nominal SI not populated |
| `HW` | `hwi1030P00` | 0 | direct; nominal SI not populated |

Only `SW`, `SE`, `PL`, and `FDI` occur as the leading species of the 16
TSA24 managed AUs; `SE` uses the SW table as its interior volume surrogate.
Every AU table therefore has a non-zero nominal site index.

## 3. Coverage

- AUs: **16** of 16 TSA24 managed-curve AUs in `03_input-tsa24.csv`.
- Ages: **36** per AU (0–350 by 10 years); **576** AU-age rows.
- Species tables: `sw 0530P00`, `pli0530P00`, `fdi0535P00`.
- Inputs checked: `04_output-tsa24.csv` `MVcon_*` equals
  `tipsy_curves_tsa24.csv` `Yield` on every AU-age row.  The compile step
  fails closed on a mismatch.

| au_id | stratum_code | si_level | bec_zone | leading_species | taf_table | taf_nominal_site_index | au_site_index | planted_density_tph | taf_run_initial_density | extrapolated_ages |
|---|---|---|---|---|---|---|---|---|---|---|
| 21002 | SBS_PLI | L | SBS | PL | pli0530P00 | 23 | 12.9 | 1700.0 | 1600 | True |
| 21007 | SBS_SX+AT | L | SBS | SW | sw 0530P00 | 20 | 13.7 | 1600.0 | 1600 | False |
| 21008 | SBS_FDI | L | SBS | FDI | fdi0535P00 | 25 | 15.7 | 1600.0 | 1600 | True |
| 22000 | SBS_SX | M | ICH | SW | sw 0530P00 | 20 | 13.8 | 1600.0 | 1600 | False |
| 22002 | SBS_PLI | M | SBS | PL | pli0530P00 | 23 | 15.5 | 1700.0 | 1600 | True |
| 22003 | SBS_BL | M | SBS | SW | sw 0530P00 | 20 | 12.7 | 2500.0 | 2500 | False |
| 22004 | ESSF_SE | M | ESSF | SE | sw 0530P00 | 20 | 10.5 | 1500.0 | 1600 | False |
| 22007 | SBS_SX+AT | M | SBS | SW | sw 0530P00 | 20 | 16.8 | 1600.0 | 1600 | False |
| 22008 | SBS_FDI | M | SBS | FDI | fdi0535P00 | 25 | 18.0 | 1600.0 | 1600 | True |
| 23000 | SBS_SX | H | ICH | SW | sw 0530P00 | 20 | 17.9 | 1600.0 | 1600 | False |
| 23001 | ESSF_BL | H | ESSF | SE | sw 0530P00 | 20 | 11.1 | 1500.0 | 1600 | False |
| 23002 | SBS_PLI | H | SBS | PL | pli0530P00 | 23 | 19.0 | 1700.0 | 1600 | True |
| 23003 | SBS_BL | H | SBS | SW | sw 0530P00 | 20 | 16.8 | 2500.0 | 2500 | False |
| 23004 | ESSF_SE | H | ESSF | SE | sw 0530P00 | 20 | 13.1 | 1500.0 | 1600 | False |
| 23007 | SBS_SX+AT | H | BWBS | SW | sw 0530P00 | 20 | 21.3 | 1600.0 | 1600 | False |
| 23008 | SBS_FDI | H | SBS | FDI | fdi0535P00 | 25 | 20.6 | 1600.0 | 1600 | True |

`extrapolated_ages=True` means the standard age grid extends beyond the last
TAF age with positive merchantable volume.  Those rows are held flat and are
flagged by `taf_extrapolated` in the tables.  Most pilot matches are below the
extrapolation threshold; the FDI and PL tables are the limiting ones.

Note: `bec_zone` comes from the TSA24 input row, while `stratum_code`/`si_level`
come from `au_table.csv`.  The two are not always identical (for example AU
22000 is `ICH` in the input but `SBS_SX` in the AU table).  The compiled table
preserves both rather than collapsing them.

## 4. Output columns

`managed_au_curves.csv` (576 rows):

| Group | Columns |
|---|---|
| Keys | `au_id`, `au_table_au_id`, `managed_curve_id`, `stratum_code`, `si_level`, `leading_species` |
| TAF provenance | `taf_table`, `taf_table_species`, `taf_nominal_site_index`, `au_site_index`, `planted_density_tph` |
| Base curve | `age`, `volume`, `height`, `dbhq`, `tph`, `gross_yield`, `crown_cover` |
| Grades (scaled, m³/ha) | `Logs_Grade_D/F/H/I/J/U/X/Y` |
| Residual fibre (scaled, ODT/ha) | `Residual_Chips_ODT_ha`, `Residual_Sawdust_ODT_ha`, `Residual_Shavings_ODT_ha`, `Residual_Trim_ODT_ha`, `Residual_Bark_ODT_ha`, `residual_fibre_odt_ha` |
| TAF audit values | `taf_volume125_m3ha`, `taf_grade_sum_m3ha`, `taf_residual_fibre_odt_ha`, `taf_grade_scale`, `taf_residue_scale`, `taf_extrapolated`, `Residual_*_taf_nominal` |
| Accounting | `grade_unallocated_m3ha`, `grade_coverage_fraction`, `residue_odt_per_m3` |

`managed_au_industrial_sorts.csv` (576 rows) carries the 20 raw TIPSY
`Industrial_Logs_*` volumes at nominal site index for share comparison.

`species_grade_curves.csv` (216 rows) carries the six species tables on the
same age grid for pilot plots that have no managed AU curve.  It is a fallback
surface, not an AU assignment.

`au_grade_coverage.csv` (16 rows) records the AU → table → run-block mapping,
site-index delta, and extrapolation flag.

## 5. Transformations and limitations

- **Share-preserving grade rescale.**  Raw TAF grade shares are kept; the grade
  total is scaled to the FEMIC managed volume for the same AU and age.  The
  grade columns therefore sum to `volume` except at very young ages where the
  TAF has no grade allocation.  `grade_unallocated_m3ha` records that residual.
- **Nominal site index.**  The TAF tables are surfaces for SW SI 20, PLI SI 23,
  and FDI SI 25.  The TSA24 AU site indices range from 10.5 to 21.3.  The
  compiled grade **shares** are the TAF shares; absolute grade volumes are
  anchored to FEMIC managed volume, not to an independent AU-SI grade run.
- **Species surrogates.**  SE and BL use the SW table because this TIPSY
  database has no SE or BL table.  `vriSpecies.txt` maps their interior volume
  surrogate to SW.  This is a surrogate for the whole grade surface, not a
  species-specific grade model.
- **Residual fibre is mill residue.**  TIPSY `Residual_Chips`, `Sawdust`,
  `Shavings`, `Trim`, and `Bark` are processing residues.  The pilot residue is
  harvest slash (`taper total - recovered logs`).  The two are reported side by
  side but are not equivalent.
- **Model output, not field grade.**  `Logs_Grade_*` is TIPSY/SYLVER model
  output.  It is not an official BC scale grade and carries no defect, sweep,
  knot, or rot observation.

## 6. Provenance

| Item | SHA-256 |
|---|---|
| `03_input-tsa24.csv` | `e3c518bdad74a7b7897d44da6d36d93f513bcbfc29495123a7a91b5b24566042` |
| `04_output-tsa24.csv` | `3939e5ef4d2bc17a50218dabd5e0f32d452fea69c135de8a29a7aec265b8759b` |
| `tipsy_curves_tsa24.csv` | `83765a61aef631b3a876fe7e7b9dfbcda6d6a4a9bcc59987607107c187763469` |
| `au_table.csv` | `fbaeb44b241e73373dfa0cf9b730cafed0f3e6f15f944056d35268d4b06b3099` |
| `Database/sw 0530P00.taf` | `e014babd67fc6d366a4a60a9452af7ae71277ca81f01b59aaea1aae8f74e628e` |
| `Database/pli0530P00.taf` | `e9744c721b8429dc460198e6d622027f0ecb734d3e754c5eece63d08d978da02` |
| `Database/fdi0535P00.taf` | `71586bfb336ed38e8b5558b063078db5436259a685633639485d8786dac432a7` |

> The PLI hash in this table must match `manifest.json`; the manifest is the
> authority if a transcription differs.

Source citation:

```text
Province of British Columbia
TIPSY 4.5
Database/<file>
Ministry Standard Database, February 2022
```

Extraction layer: `fresh-tipsy` `parse_taf_file` + `tab-taf-columns.csv`.

Output hashes are in `data/derived/national/bucking/tsa24_grade_curves/manifest.json`.

## 7. Validation join

`validate_tsa24.py` maps each pilot plot to a TSA24 managed AU with the same
join used by the TIPSY volume benchmark:

```text
FAIB plot
  -> BEC + leading supported species stratum_code
  -> within-stratum PSP site-index tertile -> L/M/H
  -> au_table managed source AU -> TSA24 managed curve AU
  -> interpolate TIPSY .taf at FAIB stand age
```

Plots without a managed AU curve use the leading-species TAF table and are
labelled `species_curve`.  Plots with no TAF table (for example EP) are
labelled `no_match` and are excluded from share metrics.

The comparison is reported as:

- exact `Industrial_Logs_*` code shares (pilot `D125L50` is aliased to TIPSY
  `D125L5`; the pilot rule spells the 5.0 m pulpwood sort `D125L50`);
- diameter-class and length-class marginal shares;
- TIPSY `Logs_Grade_*` shares as a proxy only, because the pilot has
  `grade_status=not_assigned`;
- residue ODT/ha and ODT/m³ with the mill-vs-harvest caveat;
- no value comparison, because no same-basis interior grade price vector is
  available.
