# Operable 100/119/150 Mm3 WS4 Forestry Residue Handoff to OSeCAN

**Artifact:** `forestry_osecan_handoff_ws4_operable_cases` **Version:** 1.0.0

**Status:** pass. Built from the operable 100-year WS4 case
chains. The official OSeCAN tree, handoff v10, residue curve v9, chain v5.1,
and the full-forest case artifacts are unchanged.

**Labels:** `model_estimate=true`, `observed=false`, `policy_grade=false`,
`national_claim=false`, `ws4_derived=true`, `sustainable_schedule=true`,
`share_based_operable_proxy=true`, `legal_thlb=false`, `slope_screen=false`,
`transformed_curves=true`, `official_osecan_changed=false`,
`chain_v51_unchanged=true`.

## 1. Method

The existing WS4 origin-province handoff logic is applied to the three
operable chains. Residue totals are projected from the operable WS4 harvest by
origin province using the frozen handoff-v10 province-to-zone weights and the
frozen v9 process/harvest definitions. Supply-curve tiers use the frozen v5.1
thresholds. Tier positions are compared with handoff v10 and reported; a
changed position is a finding, not an official OSeCAN change.

## 2. Tier positions

| Case | Basis | Stream | Case | National PJ | Tier | v10 PJ | v10 tier |
|---|---|---|---|---:|---|---:|---|
| 100m | operable_100m | process | process_availability_000 | 0.000000 | T1 | 0.000000 | T1 |
| 100m | operable_100m | process | process_availability_025 | 107.221839 | T2 | 104.809505 | T2 |
| 100m | operable_100m | process | process_availability_050 | 214.443677 | above_T4 | 209.619009 | T4 |
| 100m | operable_100m | process | process_availability_075 | 321.665516 | above_T4 | 314.428514 | above_T4 |
| 100m | operable_100m | harvest | harvest_recovery_035 | 133.789711 | T3 | 130.635373 | T3 |
| 100m | operable_100m | harvest | harvest_recovery_060 | 229.353790 | above_T4 | 223.946354 | above_T4 |
| 100m | operable_100m | harvest | harvest_recovery_075 | 286.692237 | above_T4 | 279.932942 | above_T4 |
| 100m | sustainable_achieved | process | process_availability_000 | 0.000000 | T1 | 0.000000 | T1 |
| 100m | sustainable_achieved | process | process_availability_025 | 105.455113 | T2 | 104.809505 | T2 |
| 100m | sustainable_achieved | process | process_availability_050 | 210.910226 | T4 | 209.619009 | T4 |
| 100m | sustainable_achieved | process | process_availability_075 | 316.365339 | above_T4 | 314.428514 | above_T4 |
| 100m | sustainable_achieved | harvest | harvest_recovery_035 | 130.870287 | T3 | 130.635373 | T3 |
| 100m | sustainable_achieved | harvest | harvest_recovery_060 | 224.349063 | above_T4 | 223.946354 | above_T4 |
| 100m | sustainable_achieved | harvest | harvest_recovery_075 | 280.436328 | above_T4 | 279.932942 | above_T4 |
| 119m | operable_119m | process | process_availability_000 | 0.000000 | T1 | 0.000000 | T1 |
| 119m | operable_119m | process | process_availability_025 | 124.828171 | T3 | 124.687729 | T3 |
| 119m | operable_119m | process | process_availability_050 | 249.656342 | above_T4 | 249.375458 | above_T4 |
| 119m | operable_119m | process | process_availability_075 | 374.484513 | above_T4 | 374.063188 | above_T4 |
| 119m | operable_119m | harvest | harvest_recovery_035 | 155.595383 | T4 | 155.543768 | T4 |
| 119m | operable_119m | harvest | harvest_recovery_060 | 266.734942 | above_T4 | 266.646460 | above_T4 |
| 119m | operable_119m | harvest | harvest_recovery_075 | 333.418677 | above_T4 | 333.308075 | above_T4 |
| 119m | sustainable_achieved | process | process_availability_000 | 0.000000 | T1 | 0.000000 | T1 |
| 119m | sustainable_achieved | process | process_availability_025 | 121.819984 | T3 | 124.687729 | T3 |
| 119m | sustainable_achieved | process | process_availability_050 | 243.639968 | above_T4 | 249.375458 | above_T4 |
| 119m | sustainable_achieved | process | process_availability_075 | 365.459952 | above_T4 | 374.063188 | above_T4 |
| 119m | sustainable_achieved | harvest | harvest_recovery_035 | 148.776066 | T3 | 155.543768 | T4 |
| 119m | sustainable_achieved | harvest | harvest_recovery_060 | 255.044684 | above_T4 | 266.646460 | above_T4 |
| 119m | sustainable_achieved | harvest | harvest_recovery_075 | 318.805855 | above_T4 | 333.308075 | above_T4 |
| 150m | operable_150m | process | process_availability_000 | 0.000000 | T1 | 0.000000 | T1 |
| 150m | operable_150m | process | process_availability_025 | 156.871529 | T4 | 156.716305 | T4 |
| 150m | operable_150m | process | process_availability_050 | 313.743058 | above_T4 | 313.432610 | above_T4 |
| 150m | operable_150m | process | process_availability_075 | 470.614587 | above_T4 | 470.148915 | above_T4 |
| 150m | operable_150m | harvest | harvest_recovery_035 | 200.628836 | T4 | 200.593895 | T4 |
| 150m | operable_150m | harvest | harvest_recovery_060 | 343.935147 | above_T4 | 343.875248 | above_T4 |
| 150m | operable_150m | harvest | harvest_recovery_075 | 429.918934 | above_T4 | 429.844060 | above_T4 |
| 150m | sustainable_achieved | process | process_availability_000 | 0.000000 | T1 | 0.000000 | T1 |
| 150m | sustainable_achieved | process | process_availability_025 | 140.392053 | T3 | 156.716305 | T4 |
| 150m | sustainable_achieved | process | process_availability_050 | 280.784107 | above_T4 | 313.432610 | above_T4 |
| 150m | sustainable_achieved | process | process_availability_075 | 421.176160 | above_T4 | 470.148915 | above_T4 |
| 150m | sustainable_achieved | harvest | harvest_recovery_035 | 169.440189 | T4 | 200.593895 | T4 |
| 150m | sustainable_achieved | harvest | harvest_recovery_060 | 290.468896 | above_T4 | 343.875248 | above_T4 |
| 150m | sustainable_achieved | harvest | harvest_recovery_075 | 363.086120 | above_T4 | 429.844060 | above_T4 |

## 3. Comparison with handoff v10

| Scenario | Stream | Case | Frozen v5.1 | v10 | WS4 primary | WS4 achieved |
|---|---|---|---|---|---|---|
| 100m | process | process_availability_000 | T1 | T1 | T1 | T1 |
| 100m | process | process_availability_025 | T2 | T2 | T2 | T2 |
| 100m | process | process_availability_050 | T4 | T4 | above_T4 | T4 |
| 100m | process | process_availability_075 | above_T4 | above_T4 | above_T4 | above_T4 |
| 100m | harvest | harvest_recovery_035 | T3 | T3 | T3 | T3 |
| 100m | harvest | harvest_recovery_060 | above_T4 | above_T4 | above_T4 | above_T4 |
| 100m | harvest | harvest_recovery_075 | above_T4 | above_T4 | above_T4 | above_T4 |
| 119m | process | process_availability_000 | T1 | T1 | T1 | T1 |
| 119m | process | process_availability_025 | T3 | T3 | T3 | T3 |
| 119m | process | process_availability_050 | above_T4 | above_T4 | above_T4 | above_T4 |
| 119m | process | process_availability_075 | above_T4 | above_T4 | above_T4 | above_T4 |
| 119m | harvest | harvest_recovery_035 | T4 | T4 | T4 | T3 |
| 119m | harvest | harvest_recovery_060 | above_T4 | above_T4 | above_T4 | above_T4 |
| 119m | harvest | harvest_recovery_075 | above_T4 | above_T4 | above_T4 | above_T4 |
| 150m | process | process_availability_000 | T1 | T1 | T1 | T1 |
| 150m | process | process_availability_025 | T4 | T4 | T4 | T3 |
| 150m | process | process_availability_050 | above_T4 | above_T4 | above_T4 | above_T4 |
| 150m | process | process_availability_075 | above_T4 | above_T4 | above_T4 | above_T4 |
| 150m | harvest | harvest_recovery_035 | T4 | T4 | T4 | T4 |
| 150m | harvest | harvest_recovery_060 | above_T4 | above_T4 | above_T4 | above_T4 |
| 150m | harvest | harvest_recovery_075 | above_T4 | above_T4 | above_T4 | above_T4 |

Frozen v5.1 reference positions: 21/21.
Operable primary/achieved matches: 100 Mm3
6/7 and 7/7;
119 Mm3 7/7 and
6/7; 150 Mm3
7/7 and
6/7.

## 4. Boundary

- The operable chains are share-based landbase proxies, not legal THLB.
- No slope or spatial road screen is applied.
- The official OSeCAN tree is unchanged (146 files, 80caa91c3e91c890..., changed_files=0).
- No chain v5.1, full-forest case, or UI artifact is changed.
