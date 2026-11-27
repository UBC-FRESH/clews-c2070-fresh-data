# Operable 100/119/150 Mm3 WS4 Forestry Residue Handoff to OSeCAN

**Artifact:** `forestry_osecan_handoff_ws4_operable_cases` **Version:** 1.0.0

**Status:** pass. Built from the operable 100-year WS4 case
chains. The official OSeCAN tree, handoff v10, residue curve v9, chain v5.1,
and the full-forest case artifacts are unchanged.

**Labels:** `model_estimate=true`, `observed=false`, `policy_grade=false`,
`national_claim=false`, `ws4_derived=true`, `sustainable_schedule=true`,
`share_based_operable_proxy=true`, `legal_thlb=false`, `slope_screen=false`,
`official_osecan_changed=false`, `chain_v51_unchanged=true`.

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
| 100m | operable_100m | process | process_availability_025 | 107.445782 | T2 | 104.809505 | T2 |
| 100m | operable_100m | process | process_availability_050 | 214.891564 | above_T4 | 209.619009 | T4 |
| 100m | operable_100m | process | process_availability_075 | 322.337346 | above_T4 | 314.428514 | above_T4 |
| 100m | operable_100m | harvest | harvest_recovery_035 | 134.113434 | T3 | 130.635373 | T3 |
| 100m | operable_100m | harvest | harvest_recovery_060 | 229.908745 | above_T4 | 223.946354 | above_T4 |
| 100m | operable_100m | harvest | harvest_recovery_075 | 287.385931 | above_T4 | 279.932942 | above_T4 |
| 100m | sustainable_achieved | process | process_availability_000 | 0.000000 | T1 | 0.000000 | T1 |
| 100m | sustainable_achieved | process | process_availability_025 | 103.428843 | T2 | 104.809505 | T2 |
| 100m | sustainable_achieved | process | process_availability_050 | 206.857686 | T4 | 209.619009 | T4 |
| 100m | sustainable_achieved | process | process_availability_075 | 310.286528 | above_T4 | 314.428514 | above_T4 |
| 100m | sustainable_achieved | harvest | harvest_recovery_035 | 129.047692 | T3 | 130.635373 | T3 |
| 100m | sustainable_achieved | harvest | harvest_recovery_060 | 221.224615 | above_T4 | 223.946354 | above_T4 |
| 100m | sustainable_achieved | harvest | harvest_recovery_075 | 276.530769 | above_T4 | 279.932942 | above_T4 |
| 119m | operable_119m | process | process_availability_000 | 0.000000 | T1 | 0.000000 | T1 |
| 119m | operable_119m | process | process_availability_025 | 124.865406 | T3 | 124.687729 | T3 |
| 119m | operable_119m | process | process_availability_050 | 249.730813 | above_T4 | 249.375458 | above_T4 |
| 119m | operable_119m | process | process_availability_075 | 374.596219 | above_T4 | 374.063188 | above_T4 |
| 119m | operable_119m | harvest | harvest_recovery_035 | 155.800013 | T4 | 155.543768 | T4 |
| 119m | operable_119m | harvest | harvest_recovery_060 | 267.085736 | above_T4 | 266.646460 | above_T4 |
| 119m | operable_119m | harvest | harvest_recovery_075 | 333.857170 | above_T4 | 333.308075 | above_T4 |
| 119m | sustainable_achieved | process | process_availability_000 | 0.000000 | T1 | 0.000000 | T1 |
| 119m | sustainable_achieved | process | process_availability_025 | 118.765454 | T3 | 124.687729 | T3 |
| 119m | sustainable_achieved | process | process_availability_050 | 237.530908 | above_T4 | 249.375458 | above_T4 |
| 119m | sustainable_achieved | process | process_availability_075 | 356.296362 | above_T4 | 374.063188 | above_T4 |
| 119m | sustainable_achieved | harvest | harvest_recovery_035 | 146.115605 | T3 | 155.543768 | T4 |
| 119m | sustainable_achieved | harvest | harvest_recovery_060 | 250.483894 | above_T4 | 266.646460 | above_T4 |
| 119m | sustainable_achieved | harvest | harvest_recovery_075 | 313.104868 | above_T4 | 333.308075 | above_T4 |
| 150m | operable_150m | process | process_availability_000 | 0.000000 | T1 | 0.000000 | T1 |
| 150m | operable_150m | process | process_availability_025 | 156.825477 | T4 | 156.716305 | T4 |
| 150m | operable_150m | process | process_availability_050 | 313.650954 | above_T4 | 313.432610 | above_T4 |
| 150m | operable_150m | process | process_availability_075 | 470.476432 | above_T4 | 470.148915 | above_T4 |
| 150m | operable_150m | harvest | harvest_recovery_035 | 200.747632 | T4 | 200.593895 | T4 |
| 150m | operable_150m | harvest | harvest_recovery_060 | 344.138797 | above_T4 | 343.875248 | above_T4 |
| 150m | operable_150m | harvest | harvest_recovery_075 | 430.173496 | above_T4 | 429.844060 | above_T4 |
| 150m | sustainable_achieved | process | process_availability_000 | 0.000000 | T1 | 0.000000 | T1 |
| 150m | sustainable_achieved | process | process_availability_025 | 139.285187 | T3 | 156.716305 | T4 |
| 150m | sustainable_achieved | process | process_availability_050 | 278.570374 | above_T4 | 313.432610 | above_T4 |
| 150m | sustainable_achieved | process | process_availability_075 | 417.855561 | above_T4 | 470.148915 | above_T4 |
| 150m | sustainable_achieved | harvest | harvest_recovery_035 | 168.534333 | T4 | 200.593895 | T4 |
| 150m | sustainable_achieved | harvest | harvest_recovery_060 | 288.916000 | above_T4 | 343.875248 | above_T4 |
| 150m | sustainable_achieved | harvest | harvest_recovery_075 | 361.145000 | above_T4 | 429.844060 | above_T4 |

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
