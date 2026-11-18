# National RSYC 150M m3 log/yr supply in OSeCAN

Status: **FRESH-side provisional** — not an official C2070 result. The experiment uses a disposable copy of public `deltae/C2070` commit `40d5b43bb3f8`; the public clone was not modified.

## Supply math (150M log -> total m3 -> ODT -> PJ; BC/rest split)

| Step | Value |
|---|---:|
| Annual log volume (m3/yr) | 150,000,000 |
| Log share of total volume | 0.762716956 |
| Total volume (m3/yr) | 196,665,354 |
| Tile-mix factor (ODT/m3 total) | 0.088317764529 |
| Gross residue (ODT/yr) | 17,369,044.40 |

| Case | Recovery | National PJ/yr | BC zonal PJ/yr | Rest-of-Canada PJ/yr | Cost ($/GJ) |
|---|---:|---:|---:|---:|---:|
| base | 0.60 | 192.796 | 43.524 | 149.273 | 2.456978 |
| low | 0.35 | 112.465 | 43.524 | 68.941 | 3.194071 |
| high | 0.75 | 240.995 | 43.524 | 197.472 | 1.965582 |

The BC zonal total is the 2028+ sum of the unchanged `SUPBCWB1` (3.605475 PJ) and `SUPBCWB2` (39.918341 PJ) caps.  The `SUPBCW` cap is recomputed year by year as national total minus the two zonal caps, which removes the 2021-2027 zonal phase-down from the national pool and keeps the three caps equal to the national total in every year.

## Parameter files/harmonize

| File | Content |
|---|---|
| `SUPBCW_activity_limits_national_150m.csv` | base rest-of-Canada cap, 2021-2070 |
| `SUPBCW_activity_limits_national_150m_low.csv` | low-recovery rest-of-Canada cap |
| `SUPBCW_activity_limits_national_150m_high.csv` | high-recovery rest-of-Canada cap |
| `SUPBCW_variable_cost_{base,low,high}.csv` | 2.456978, 3.194071, 1.965582 $/GJ |
| `supply_basis.json` | full conversion and cap-split record |

`osecan harmonize` returned exit 0 for the base parameters and for all three scenario parameter sets: **HARMONIZED — all params reference valid SET codes.**  `PWRBCWB1`/`PWRBCWB2` consume `BCWB1`/`BCWB2`; the other eleven `PWRBCW<z>` plants consume the national `BCW` pool.

## Baseline (objective, dispatch, binding, emissions)

`Current Measures`, 2021-2070, CO2 95 $/t to 2025 and 115 $/t thereafter, normal hydro, national base cap 149.273 PJ (2028+).

| Metric | Baseline | Stress $200/hydro-frozen | Δ stress |
|---|---:|---:|---:|
| Solver status | optimal | optimal | — |
| Objective (M$) | 1,331,289.52 | 1,370,983.13 | 39,693.61 |
| Emissions total (Mt) | 25.715 | 38.545 | 12.830 |

### SUP activity by year (PJ)

| Run / technology | 2021 | 2025 | 2028 | 2030 | 2050 | 2070 | Total |
|---|---:|---:|---:|---:|---:|---:|---:|
| baseline / `SUPBCW` | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| baseline / `SUPBCWB1` | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| baseline / `SUPBCWB2` | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| stress / `SUPBCW` | 0.000 | 95.868 | 149.273 | 149.273 | 149.273 | 149.273 | 6,946.907 |
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
| stress / `PWRBCW` other zones | 0.000 | 25.771 | 40.127 | 40.127 | 40.127 | 40.127 | 1,867.448 |

### Cap binding

| Run | Technology | Cap binds | Binding years | Count | Max utilisation |
|---|---|---|---|---:|---:|
| baseline | `SUPBCW` | no | — | 0 | 0.000 |
| baseline | `SUPBCWB1` | no | — | 0 | 0.000 |
| baseline | `SUPBCWB2` | no | — | 0 | 0.000 |
| stress | `SUPBCW` | yes | 2028-2070 | 43 | 1.000 |
| stress | `SUPBCWB1` | yes | 2026-2070 | 45 | 1.000 |
| stress | `SUPBCWB2` | yes | 2032-2070 | 39 | 1.000 |
| baseline_bio | `SUPBCW` | no | — | 0 | 0.000 |
| baseline_bio | `SUPBCWB1` | no | — | 0 | 0.000 |
| baseline_bio | `SUPBCWB2` | no | — | 0 | 0.000 |

### PWRBCW dispatch outside B1/B2 (PJ, total 2021-2070)

| Zone | Baseline | Stress |
|---|---:|---:|
| A1 | 0.000 | 289.771 |
| A2 | 0.000 | 235.858 |
| L1 | 0.000 | 69.109 |
| M1 | 0.000 | 41.562 |
| N1 | 0.000 | 0.000 |
| O1 | 0.000 | 174.878 |
| O2 | 0.000 | 39.697 |
| Q1 | 0.000 | 101.448 |
| Q2 | 0.000 | 250.328 |
| S1 | 0.000 | 414.759 |
| T1 | 0.000 | 250.038 |

### Emissions

| Run | 2021 | 2025 | 2030 | 2050 | 2070 | Total (Mt) |
|---|---:|---:|---:|---:|---:|---:|
| baseline | 0.017 | 0.000 | 1.031 | 1.031 | 0.000 | 25.715 |
| stress | 0.023 | 0.241 | 1.465 | 1.488 | 0.000 | 38.545 |
| baseline_bio | 0.017 | 0.000 | 1.031 | 1.031 | 0.000 | 25.715 |

## Stress $200/hydro-frozen

The stress run raises the 2026+ carbon price from 115 to 200 $/t and fixes every `PWRHYD<z>` at its 2021 base activity.  It keeps the same national/zonal caps and costs as the baseline.

Objective 1,370,983.13 M$ vs baseline 1,331,289.52 M$ (39,693.61 M$); cumulative CO2 38.545 Mt vs 25.715 Mt.  In the stress run `SUPBCW` binds in 2028-2070 (43 years), `SUPBCWB1` in 2026-2070 and `SUPBCWB2` in 2032-2070.

### Comparison to the 50 PJ placeholder and the BC zonal 43.5238 PJ run

| Run | Forcing | Objective (M$) | Emissions (Mt) | BCW supply (PJ) |
|---|---|---:|---:|---:|
| 50 PJ placeholder | baseline (95/115 $/t, normal hydro) | 1,331,287.25 | 25.750 | 0.000 |
| National 150M baseline | baseline (95/115 $/t, normal hydro) | 1,331,289.52 | 25.715 | 0.000 |
| BC zonal 43.5238 PJ | stress (200 $/t, hydro frozen) | 1,371,599.09 | 61.659 | 1,872.589 |
| National 150M stress | stress (200 $/t, hydro frozen) | 1,370,983.13 | 38.545 | 8,819.496 |

At the baseline carbon schedule gas outcompetes biomass, so all three biomass supply technologies are zero and the national cap is slack; the 150M cap changes the objective only by the small `SUPBCW` cost difference relative to the 50 PJ placeholder.  Under the stress forcing the national cap binds and supplies about 8.8 EJ over 2021-2070, versus 1.87 EJ in the BC-only zonal run, lowering cumulative CO2 from 61.659 to 38.545 Mt.

## Generic-BIO sensitivity

The `baseline_bio` run raises `RNWBIO` VariableCost from 3.00 to 4.00 $/GJ on the baseline forcing.  This is a documented biomass-wide bypass sensitivity, not a dedicated power-biomass supply curve.

| Metric | Baseline | Baseline + BIO | Δ |
|---|---:|---:|---:|
| Objective (M$) | 1,331,289.52 | 1,344,942.45 | 13,652.93 |
| Emissions total (Mt) | 25.715 | 25.715 | 0.000 |
| `SUPBCW` total (PJ) | 0.000 | 0.000 | 0.000 |
| BC zonal total (PJ) | 0.000 | 0.000 | 0.000 |
| `PWRBIO` total (PJ) | 0.000 | 0.000 | 0.000 |

## Tests/commits/publish/status

Tests cover the cap split (`SUPBCW + SUPBCWB1 + SUPBCWB2 = national total` in every year) and the 150M log -> total m3 -> ODT -> PJ conversion against the fixed tile-supply outputs.

## Caveats (RSYC-only, no AAC/THLB, B25, group curves)

- RSYC-only v0: no local corrections; benchmark correction factors withheld.
- No adopted national AAC, THLB, or operability filter is applied.
- B25 is flagged over capacity in the tile library (1.216 ratio) and is not clipped.
- Group cells (BROADLEAF, CONIFER) use group RSYC curves; generic cells use the tile generic curve.
- The 150M log basis is an annual supply assumption, not a harvest forecast.
- The BC zonal total is the 2028+ steady state; 2021-2027 zonal caps phase down from historic levels.
