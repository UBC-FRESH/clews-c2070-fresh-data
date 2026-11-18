# National OSeCAN base at the 2024 observed harvest: 118,977,339 m3 log/yr

Status: **FRESH-side provisional** — not an official C2070 result. The experiment uses a disposable copy of public `deltae/C2070` commit `40d5b43bb3f8`; the public clone was not modified.

## Harvest basis

The base is the FSD 2024 national observed harvest of **118,977,339 m3/yr**, not the former 150M scenario assumption. FSD 2021-2024 provincial values fill the harvest template; 2024 is held flat from 2025 as a documented accounting path.  The 150M case is an upper bound, 26.1% above the observed 2024 level.

| Case | 2024 log basis (m3/yr) | Status |
|---|---:|---|
| Observed 2024 | 118,977,339 | FSD observation, used here |
| 100M | 100,000,000 | lower scenario bound |
| 150M | 150,000,000 | upper scenario bound, not central |
| 200M | 200,000,000 | stress bound |

## Supply math (119M log -> total m3 -> ODT -> PJ; BC/rest split)

| Step | Value |
|---|---:|
| Annual log volume (m3/yr) | 118,977,339 |
| Log share of total volume | 0.762716956 |
| Total volume (m3/yr) | 155,991,469.70 |
| Tile-mix factor (ODT/m3 total) | 0.088317764529 |
| Gross residue (ODT/yr) | 13,776,817.89 |

| Case | Recovery | National PJ/yr | BC zonal PJ/yr | Rest-of-Canada PJ/yr | Cost ($/GJ) |
|---|---:|---:|---:|---:|---:|
| base | 0.60 | 152.923 | 43.524 | 109.399 | 2.456978 |
| low | 0.35 | 89.205 | 43.524 | 45.681 | 3.194071 |
| high | 0.75 | 191.153 | 43.524 | 147.630 | 1.965582 |

The BC zonal total is the 2028+ sum of the unchanged `SUPBCWB1` (3.605475 PJ) and `SUPBCWB2` (39.918341 PJ) caps.  The `SUPBCW` cap is recomputed year by year as national total minus the two zonal caps, so `SUPBCW + SUPBCWB1 + SUPBCWB2` equals the national total in every year without double counting BC.

## Parameter files / harmonize

| File | Content |
|---|---|
| `SUPBCW_activity_limits_national_base_119m.csv` | base rest-of-Canada cap, 2021-2070 |
| `SUPBCW_activity_limits_national_base_119m_low.csv` | low-recovery rest-of-Canada cap |
| `SUPBCW_activity_limits_national_base_119m_high.csv` | high-recovery rest-of-Canada cap |
| `SUPBCW_variable_cost_{base,low,high}.csv` | 2.456978, 3.194071, 1.965582 $/GJ |
| `supply_basis.json` | full conversion and cap-split record |

`osecan harmonize` evidence recorded: base exit 0 (SHA-256 b692fd21f743…), baseline_119m exit 0 (SHA-256 8e517e4e5ff3…), stress_119m exit 0 (SHA-256 783e76336532…).  **HARMONIZED — all params reference valid SET codes.**  `PWRBCWB1`/`PWRBCWB2` consume `BCWB1`/`BCWB2`; the other eleven `PWRBCW<z>` plants consume the national `BCW` pool.

## Baseline (objective, dispatch, binding, emissions)

`Current Measures`, 2021-2070, CO2 95 $/t to 2025 and 115 $/t thereafter, normal hydro, national base cap 109.399 PJ (2028+).

| Metric | Baseline | Stress $200/hydro-capped | Δ stress |
|---|---:|---:|---:|
| Solver status | optimal | optimal | — |
| Objective (M$) | 1,331,289.52 | 1,371,124.38 | 39,834.86 |
| Emissions total (Mt) | 25.715 | 38.545 | 12.830 |
| `PWRHYDB2` 2021 dispatch (PJ) | 62.479153 | 62.410055 | -0.069098 |

### SUP activity by year (PJ)

| Run / technology | 2021 | 2025 | 2028 | 2030 | 2050 | 2070 | Total |
|---|---:|---:|---:|---:|---:|---:|---:|
| baseline / `SUPBCW` | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| baseline / `SUPBCWB1` | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| baseline / `SUPBCWB2` | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| stress / `SUPBCW` | 0.000 | 95.868 | 109.399 | 109.399 | 109.399 | 109.399 | 5,213.950 |
| stress / `SUPBCWB1` | 0.000 | 3.605 | 3.605 | 3.605 | 3.605 | 3.605 | 165.852 |
| stress / `SUPBCWB2` | 0.000 | 3.691 | 19.357 | 35.394 | 39.918 | 39.918 | 1,706.737 |

### PWR dispatch by year (PJ electricity)

| Run / technology | 2021 | 2025 | 2028 | 2030 | 2050 | 2070 | Total |
|---|---:|---:|---:|---:|---:|---:|---:|
| baseline / `PWRBCWB1` | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| baseline / `PWRBCWB2` | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| baseline / `PWRBCW` other zones | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| stress / `PWRBCWB1` | 0.000 | 0.969 | 0.969 | 0.969 | 0.969 | 0.969 | 44.584 |
| stress / `PWRBCWB2` | 0.000 | 0.992 | 5.204 | 9.515 | 10.731 | 10.731 | 458.800 |
| stress / `PWRBCW` other zones | 0.000 | 25.771 | 29.408 | 29.408 | 29.408 | 29.408 | 1,401.599 |

### Cap binding

| Run | Technology | Cap binds | Binding years | Count | Max utilisation |
|---|---|---|---|---:|---:|
| baseline_119m | `SUPBCW` | no | — | 0 | 0.000 |
| baseline_119m | `SUPBCWB1` | no | — | 0 | 0.000 |
| baseline_119m | `SUPBCWB2` | no | — | 0 | 0.000 |
| stress_119m | `SUPBCW` | yes | 2027-2070 | 44 | 1.000 |
| stress_119m | `SUPBCWB1` | yes | 2026-2070 | 45 | 1.000 |
| stress_119m | `SUPBCWB2` | yes | 2032-2070 | 39 | 1.000 |

### PWRBCW dispatch outside B1/B2 (PJ, total 2021-2070)

| Zone | Baseline | Stress |
|---|---:|---:|
| A1 | 0.000 | 214.803 |
| A2 | 0.000 | 203.914 |
| L1 | 0.000 | 48.074 |
| M1 | 0.000 | 49.329 |
| N1 | 0.000 | 0.000 |
| O1 | 0.000 | 32.740 |
| O2 | 0.000 | 35.635 |
| Q1 | 0.000 | 138.429 |
| Q2 | 0.000 | 250.214 |
| S1 | 0.000 | 209.284 |
| T1 | 0.000 | 219.178 |

### Emissions

| Run | 2021 | 2025 | 2030 | 2050 | 2070 | Total (Mt) |
|---|---:|---:|---:|---:|---:|---:|
| baseline_119m | 0.017 | 0.000 | 1.031 | 1.031 | 0.000 | 25.715 |
| stress_119m | 0.023 | 0.241 | 1.465 | 1.488 | 0.000 | 38.545 |

## Stress $200/hydro-capped

The stress run raises the 2026+ carbon price from 115 to 200 $/t.  Its only hydro constraint is a `TotalTechnologyAnnualActivityUpperLimit` at each `PWRHYD<z>`'s 2021 base activity; it is a **cap at the 2021 activity, not fixed dispatch**.  The run keeps the same national and zonal caps and costs as the baseline.

Objective 1,371,124.38 M$ vs baseline 1,331,289.52 M$ (39,834.86 M$); cumulative CO2 38.544682 Mt vs 25.714753 Mt (12.829929 Mt vs baseline).  In the stress run `SUPBCW` binds in 2027-2070 (44 years), `SUPBCWB1` in 2026-2070 and `SUPBCWB2` in 2032-2070.

## Comparison to the 100M / 150M / 200M stress cases

| Case | Log basis (m3/yr) | Objective (M$) | Emissions (Mt) | BCW supply (PJ) | `SUPBCW` binds |
|---|---:|---:|---:|---:|---|
| 100M stress | 100,000,000 | 1,371,219.04 | 39.685 | 5,972.421 | 2024-2070 (47 yrs) |
| 150M stress | 150,000,000 | 1,370,983.13 | 38.545 | 8,819.496 | 2028-2070 (43 yrs) |
| 200M stress | 200,000,000 | 1,370,767.51 | 38.028 | 11,563.727 | 2029-2070 (42 yrs) |
| **119M base (this run)** | 118,977,339 | 1,371,124.38 | 38.545 | 7,086.539 | 2027-2070 |

The 119M case is the observed 2024 harvest basis.  The 150M case is 26.1% above it and remains an upper bound; it is retained for comparison, not promoted to the central case.  The baseline at 115 $/t is zero-biomass, so its objective and emissions are a controlled no-biomass reference; the stress run is the informative supply case.

## Tests/commits/publish/status

The cap split is checked against `SUPBCW + SUPBCWB1 + SUPBCWB2 = national total` in every year, and the conversion is checked against the fixed tile-supply outputs.  `osecan harmonize` evidence is recorded above from the disposable model copy.

## Caveats (observed hold, no forecast, managed landbase pending)

- The 2024 observed harvest is held flat from 2025; this is not a harvest forecast.
- No provincial AAC trajectory, managed land base (THLB), or operability filter is applied.
- RSYC-only v0: no local corrections; benchmark correction factors withheld.
- B25 is flagged over capacity in the tile library (1.216 ratio) and is not clipped.
- Group cells (BROADLEAF, CONIFER) use group RSYC curves; generic cells use the tile generic curve.
- The BC zonal total is the 2028+ steady state; 2021-2027 zonal caps phase down from historic levels.
- The 119M basis is an observed harvest level, not a sustainable-supply estimate.
