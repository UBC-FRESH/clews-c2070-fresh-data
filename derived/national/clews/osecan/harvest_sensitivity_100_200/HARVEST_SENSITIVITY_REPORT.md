# National harvest sensitivity: 100M and 200M m3 log/yr

Status: **FRESH-side provisional** — not an official C2070 result. The 100M and 200M stress cases were solved in a disposable copy of public `deltae/C2070` commit `40d5b43bb3f8`; neither `/tmp/osecan_national` nor any pre-existing main-repository file was modified.

## Basis and cap math

RSYC-only v0: log share `0.762716956451988` and tile-mix factor `0.08831776452936206` ODT/m3 total. `total_m3 = log / log_share`, `ODT = total_m3 * factor`, `PJ = ODT * recovery * 18.5 / 1e6`.

| Case | Log (m3/yr) | Total (m3/yr) | ODT/yr | National PJ (base) | BC zonal 2028+ (PJ) | Rest of Canada 2028+ (PJ) |
|---|---:|---:|---:|---:|---:|---:|
| 100M | 100,000,000 | 131,110,236 | 11,579,363 | 128.531 | 43.523816 | 85.007 |
| 200M | 200,000,000 | 262,220,472 | 23,158,726 | 257.062 | 43.523816 | 213.538 |

Recovery variants (not run in this sensitivity; base 0.60 is the stress supply case):

| Case | National PJ low (0.35) | National PJ base (0.60) | National PJ high (0.75) | Rest 2028+ low | Rest 2028+ base | Rest 2028+ high |
|---|---:|---:|---:|---:|---:|---:|
| 100M | 74.976 | 128.531 | 160.664 | 31.453 | 85.007 | 117.140 |
| 200M | 149.953 | 257.062 | 321.327 | 106.429 | 213.538 | 277.804 |

The `SUPBCW` cap is national minus the unchanged BC zonal caps in every year, so `SUPBCW + SUPBCWB1 + SUPBCWB2` equals the national total without double counting. The 2021-2027 BC phase-down is preserved; 2028+ is flat.

| Year | BC zonal (B1+B2) PJ | 100M `SUPBCW` PJ | 200M `SUPBCW` PJ |
|---:|---:|---:|---:|
| 2021 | 50.325738 | 78.205191 | 206.736119 |
| 2022 | 49.490560 | 79.040369 | 207.571297 |
| 2023 | 47.366174 | 81.164754 | 209.695683 |
| 2024 | 45.672388 | 82.858540 | 211.389469 |
| 2025 | 43.590223 | 84.940706 | 213.471634 |
| 2026 | 43.582091 | 84.948838 | 213.479766 |
| 2027 | 43.582091 | 84.948838 | 213.479766 |
| 2028 | 43.523816 | 85.007113 | 213.538041 |
| 2030 | 43.523816 | 85.007113 | 213.538041 |
| 2050 | 43.523816 | 85.007113 | 213.538041 |
| 2070 | 43.523816 | 85.007113 | 213.538041 |

## Stress results

`Current Measures`, 2021-2070: CO2 95 $/t to 2025 and 200 $/t from 2026; every `PWRHYD<z>` has an **upper** activity cap equal to its 2021 base activity in all years (the 150M stress definition; no fixed lower+upper).

| Metric | 100M stress | 200M stress |
|---|---:|---:|
| Solver status | optimal | optimal |
| Objective (M$) | 1,371,219.04 | 1,370,767.51 |
| Emissions total (Mt CO2) | 39.685 | 38.028 |
| BCW supply total (PJ) | 5,972.421 | 11,563.727 |
| PWRBCW dispatch total (PJ) | 1,605.489 | 3,108.529 |
| LP size (rows x cols) | 274,851 x 235,800 | 274,851 x 235,800 |

### Supply activity by year (PJ)

| Run / technology | 2021 | 2025 | 2028 | 2030 | 2050 | 2070 | Total |
|---|---:|---:|---:|---:|---:|---:|---:|
| 100M / `SUPBCW` | 0.000 | 84.941 | 85.007 | 85.007 | 85.007 | 85.007 | 4,099.832 |
| 100M / `SUPBCWB1` | 0.000 | 3.605 | 3.605 | 3.605 | 3.605 | 3.605 | 165.852 |
| 100M / `SUPBCWB2` | 0.000 | 3.691 | 19.357 | 35.394 | 39.918 | 39.918 | 1,706.737 |
| 200M / `SUPBCW` | 0.000 | 97.251 | 182.219 | 213.538 | 213.538 | 213.538 | 9,691.138 |
| 200M / `SUPBCWB1` | 0.000 | 3.605 | 3.605 | 3.605 | 3.605 | 3.605 | 165.852 |
| 200M / `SUPBCWB2` | 0.000 | 3.691 | 19.357 | 35.394 | 39.918 | 39.918 | 1,706.737 |

### PWRBCW dispatch by year (PJ electricity)

| Run / technology | 2021 | 2025 | 2028 | 2030 | 2050 | 2070 | Total |
|---|---:|---:|---:|---:|---:|---:|---:|
| 100M / `PWRBCWB1` | 0.000 | 0.969 | 0.969 | 0.969 | 0.969 | 0.969 | 44.584 |
| 100M / `PWRBCWB2` | 0.000 | 0.992 | 5.204 | 9.515 | 10.731 | 10.731 | 458.800 |
| 100M / `PWRBCW` other zones | 0.000 | 22.834 | 22.851 | 22.851 | 22.851 | 22.851 | 1,102.105 |
| 200M / `PWRBCWB1` | 0.000 | 0.969 | 0.969 | 0.969 | 0.969 | 0.969 | 44.584 |
| 200M / `PWRBCWB2` | 0.000 | 0.992 | 5.204 | 9.515 | 10.731 | 10.731 | 458.800 |
| 200M / `PWRBCW` other zones | 0.000 | 26.143 | 48.984 | 57.403 | 57.403 | 57.403 | 2,605.145 |

### Cap binding

| Run | Technology | Binds | Binding years | Count | Max utilisation |
|---|---|---|---|---:|---:|
| 100M | `SUPBCW` | yes | 2024-2070 | 47 | 1.000000 |
| 100M | `SUPBCWB1` | yes | 2026-2070 | 45 | 0.999999 |
| 100M | `SUPBCWB2` | yes | 2032-2070 | 39 | 0.999999 |
| 200M | `SUPBCW` | yes | 2029-2070 | 42 | 1.000000 |
| 200M | `SUPBCWB1` | yes | 2026-2070 | 45 | 0.999999 |
| 200M | `SUPBCWB2` | yes | 2032-2070 | 39 | 0.999999 |

### PWRBCW dispatch by zone outside B1/B2 (PJ, 2021-2070 total)

| Zone | 100M stress | 200M stress |
|---|---:|---:|
| A1 | 332.893 | 712.532 |
| A2 | 77.765 | 231.464 |
| L1 | 16.088 | 48.715 |
| M1 | 41.562 | 60.933 |
| N1 | 0.000 | 0.186 |
| O1 | 0.000 | 416.192 |
| O2 | 0.000 | 223.251 |
| Q1 | 189.219 | 277.562 |
| Q2 | 64.669 | 295.194 |
| S1 | 160.496 | 228.294 |
| T1 | 219.414 | 110.819 |

### Emissions (Mt CO2)

| Run | 2021 | 2025 | 2030 | 2050 | 2070 | Total |
|---|---:|---:|---:|---:|---:|---:|
| 100M | 0.023 | 0.279 | 1.503 | 1.526 | 0.000 | 39.685 |
| 200M | 0.034 | 0.233 | 1.448 | 1.471 | 0.000 | 38.028 |

## Comparison and interpretation

| Case | Objective (M$) | Emissions (Mt) | BCW supply (PJ) | PWRBCW dispatch (PJ) | `SUPBCW` binds | `SUPBCWB1` binds | `SUPBCWB2` binds |
|---|---:|---:|---:|---:|---|---|---|
| 100M stress | 1,371,219.04 | 39.685 | 5,972.421 | 1,605.489 | yes (2024-2070; 47 yrs) | yes (2026-2070; 45 yrs) | yes (2032-2070; 39 yrs) |
| 150M stress | 1,370,983.13 | 38.545 | 8,819.496 | 2,370.832 | yes (2028-2070; 43 yrs) | yes (2026-2070; 45 yrs) | yes (2032-2070; 39 yrs) |
| 200M stress | 1,370,767.51 | 38.028 | 11,563.727 | 3,108.529 | yes (2029-2070; 42 yrs) | yes (2026-2070; 45 yrs) | yes (2032-2070; 39 yrs) |

For context, the 150M `Current Measures` baseline at 115 $/t and normal hydro was 1,331,289.52 M$ with 25.715 Mt CO2 and zero BCW supply (known zero-biomass; not rerun).

Deltas against the 150M stress case (positive means higher than 150M):

| Case | Objective delta (M$) | Emissions delta (Mt) | BCW supply delta (PJ) |
|---|---:|---:|---:|
| 100M | 235.91 | 1.140 | -2,847.075 |
| 200M | -215.62 | -0.517 | 2,744.232 |

Interpretation:

- At 200 $/t with the 2021 hydro upper cap, **all three `SUPBCW` caps bind**: 100M in 2024-2070 (47 years), 150M in 2028-2070 (43 years), and 200M in 2029-2070 (42 years). Even the 200M rest-of-Canada pool is exhausted for most of the horizon.
- 100M vs 150M: BCW supply is 2,847.075 PJ lower, emissions are 1.140 Mt higher, and the objective is 235.91 M$ higher. The tighter cap starts binding in 2024, four years earlier than 150M.
- 200M vs 150M: BCW supply is 2,744.232 PJ higher, emissions are 0.517 Mt lower, and the objective is 215.62 M$ lower. The larger pool starts binding one year later (2029 vs 2028).
- Across the full 100M-to-200M doubling, cumulative BCW supply rises by 5,591.306 PJ, emissions fall by 1.658 Mt, and the objective falls by 451.53 M$.
- `SUPBCWB1` and `SUPBCWB2` dispatch are identical in all three cases (the BC zonal caps and costs are unchanged), so every cross-case difference comes from `SUPBCW` and the rest-of-Canada `PWRBCW<z>` plants.
- The emissions response is modest relative to the cap scaling, but the ordering is monotonic: a larger national residue pool allows more BCW generation under the stress and displaces fossil output.

## Paths and status

- Model copy: `/tmp/osecan_sens_100_200`
- Source copy (read-only basis): `/tmp/osecan_national`
- Output artifacts: `/srv/shared-data/gep/jupyterhub16-projects/clews-c2070-fresh/data/derived/national/clews/osecan/harvest_sensitivity_100_200`
- 100M run: `/tmp/osecan_sens_100_200/results/harvest_100m_stress`
- 200M run: `/tmp/osecan_sens_100_200/results/harvest_200m_stress`
- 100M solve time: 76.3 s; 200M solve time: 76.8 s
- `osecan harmonize` passed for both parameter sets; parameter CSVs round-tripped the expected caps, costs and carbon schedule.
- The copy's `src`, `data/params`, and `SETs` trees match `/tmp/osecan_national`; the runtime import resolved to `/tmp/osecan_sens_100_200/src/osecan/__init__.py`.
- `/tmp/osecan_national` was copied at start and was not modified; the main repository was only read, except for the new output directory.
- No git commit was made.

## Caveats

- The hydro stress is an **upper** cap only, at each `PWRHYD<z>` 2021 base activity. It is not a fixed lower+upper variant and is not a forecast.
- The supply basis is RSYC-only v0 with no local corrections, benchmark correction factors, AAC/THLB/operability filters, or new residue curves.
- The cap arithmetic assumes the adopted log share and tile-mix factor are constant over 2021-2070; 2028+ caps are flat.
- Results are GLPK solutions at the model's default tolerances; activity limits in the osecan datafile carry six significant figures, so solved activity can exceed the exact CSV cap by a rounding step (<1e-3 PJ).
- The copied virtual environment's editable `osecan` pointer still names `/tmp/osecan_zonal/src`. Runs were launched with `PYTHONPATH` pinned to `/tmp/osecan_sens_100_200/src`; the imported package was verified from that path and the copy's source files match the source copy.
- The copy retains the source copy's pre-existing working-tree zonal edits (`src/osecan/model_structure.py`, `src/osecan/sets_n_ratios.py`) and its `apply_scenarios.py`/`run_one.py`; these are the same files used for the 150M run.

