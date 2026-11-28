# Operable 100/119/150 Mm3 WS4 Forestry Residue Handoff to OSeCAN

**Artifact:** `forestry_osecan_handoff_ws4_operable_cases` **Version:** 1.0.0

**Status:** pass. Built from the operable 100-year WS4 case
chains. The official OSeCAN tree, handoff v10, residue curve v9, chain v5.1,
and the full-forest case artifacts are unchanged.

**Labels:** `model_estimate=true`, `observed=false`, `policy_grade=false`, `national_claim=false`, `ws4_derived=true`, `sustainable_schedule=true`, `transformed_curves=true`, `natural_5param_only=true`, `managed_basis_quarantined=true`, `official_osecan_changed=false`, `chain_v51_unchanged=true`.

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
| 100m | operable_100m | process | process_availability_025 | 87.343565 | T2 | 104.809505 | T2 |
| 100m | operable_100m | process | process_availability_050 | 174.687130 | T4 | 209.619009 | T4 |
| 100m | operable_100m | process | process_availability_075 | 262.030696 | above_T4 | 314.428514 | above_T4 |
| 100m | operable_100m | harvest | harvest_recovery_035 | 97.796005 | T2 | 130.635373 | T3 |
| 100m | operable_100m | harvest | harvest_recovery_060 | 167.650295 | T4 | 223.946354 | above_T4 |
| 100m | operable_100m | harvest | harvest_recovery_075 | 209.562868 | T4 | 279.932942 | above_T4 |
| 100m | sustainable_achieved | process | process_availability_000 | 0.000000 | T1 | 0.000000 | T1 |
| 100m | sustainable_achieved | process | process_availability_025 | 91.453562 | T2 | 104.809505 | T2 |
| 100m | sustainable_achieved | process | process_availability_050 | 182.907123 | T4 | 209.619009 | T4 |
| 100m | sustainable_achieved | process | process_availability_075 | 274.360685 | above_T4 | 314.428514 | above_T4 |
| 100m | sustainable_achieved | harvest | harvest_recovery_035 | 108.666528 | T2 | 130.635373 | T3 |
| 100m | sustainable_achieved | harvest | harvest_recovery_060 | 186.285476 | T4 | 223.946354 | above_T4 |
| 100m | sustainable_achieved | harvest | harvest_recovery_075 | 232.856845 | above_T4 | 279.932942 | above_T4 |
| 119m | operable_119m | process | process_availability_000 | 0.000000 | T1 | 0.000000 | T1 |
| 119m | operable_119m | process | process_availability_025 | 101.267093 | T2 | 124.687729 | T3 |
| 119m | operable_119m | process | process_availability_050 | 202.534185 | T4 | 249.375458 | above_T4 |
| 119m | operable_119m | process | process_availability_075 | 303.801278 | above_T4 | 374.063188 | above_T4 |
| 119m | operable_119m | harvest | harvest_recovery_035 | 112.175164 | T3 | 155.543768 | T4 |
| 119m | operable_119m | harvest | harvest_recovery_060 | 192.300281 | T4 | 266.646460 | above_T4 |
| 119m | operable_119m | harvest | harvest_recovery_075 | 240.375351 | above_T4 | 333.308075 | above_T4 |
| 119m | sustainable_achieved | process | process_availability_000 | 0.000000 | T1 | 0.000000 | T1 |
| 119m | sustainable_achieved | process | process_availability_025 | 105.957618 | T2 | 124.687729 | T3 |
| 119m | sustainable_achieved | process | process_availability_050 | 211.915237 | T4 | 249.375458 | above_T4 |
| 119m | sustainable_achieved | process | process_availability_075 | 317.872855 | above_T4 | 374.063188 | above_T4 |
| 119m | sustainable_achieved | harvest | harvest_recovery_035 | 124.132002 | T3 | 155.543768 | T4 |
| 119m | sustainable_achieved | harvest | harvest_recovery_060 | 212.797718 | T4 | 266.646460 | above_T4 |
| 119m | sustainable_achieved | harvest | harvest_recovery_075 | 265.997147 | above_T4 | 333.308075 | above_T4 |
| 150m | operable_150m | process | process_availability_000 | 0.000000 | T1 | 0.000000 | T1 |
| 150m | operable_150m | process | process_availability_025 | 118.404122 | T3 | 156.716305 | T4 |
| 150m | operable_150m | process | process_availability_050 | 236.808244 | above_T4 | 313.432610 | above_T4 |
| 150m | operable_150m | process | process_availability_075 | 355.212366 | above_T4 | 470.148915 | above_T4 |
| 150m | operable_150m | harvest | harvest_recovery_035 | 130.513657 | T3 | 200.593895 | T4 |
| 150m | operable_150m | harvest | harvest_recovery_060 | 223.737697 | above_T4 | 343.875248 | above_T4 |
| 150m | operable_150m | harvest | harvest_recovery_075 | 279.672121 | above_T4 | 429.844060 | above_T4 |
| 150m | sustainable_achieved | process | process_availability_000 | 0.000000 | T1 | 0.000000 | T1 |
| 150m | sustainable_achieved | process | process_availability_025 | 117.389555 | T3 | 156.716305 | T4 |
| 150m | sustainable_achieved | process | process_availability_050 | 234.779110 | above_T4 | 313.432610 | above_T4 |
| 150m | sustainable_achieved | process | process_availability_075 | 352.168665 | above_T4 | 470.148915 | above_T4 |
| 150m | sustainable_achieved | harvest | harvest_recovery_035 | 137.154166 | T3 | 200.593895 | T4 |
| 150m | sustainable_achieved | harvest | harvest_recovery_060 | 235.121427 | above_T4 | 343.875248 | above_T4 |
| 150m | sustainable_achieved | harvest | harvest_recovery_075 | 293.901784 | above_T4 | 429.844060 | above_T4 |

## 3. Comparison with handoff v10

| Scenario | Stream | Case | Frozen v5.1 | v10 | WS4 primary | WS4 achieved |
|---|---|---|---|---|---|---|
| 100m | process | process_availability_000 | T1 | T1 | T1 | T1 |
| 100m | process | process_availability_025 | T2 | T2 | T2 | T2 |
| 100m | process | process_availability_050 | T4 | T4 | T4 | T4 |
| 100m | process | process_availability_075 | above_T4 | above_T4 | above_T4 | above_T4 |
| 100m | harvest | harvest_recovery_035 | T3 | T3 | T2 | T2 |
| 100m | harvest | harvest_recovery_060 | above_T4 | above_T4 | T4 | T4 |
| 100m | harvest | harvest_recovery_075 | above_T4 | above_T4 | T4 | above_T4 |
| 119m | process | process_availability_000 | T1 | T1 | T1 | T1 |
| 119m | process | process_availability_025 | T3 | T3 | T2 | T2 |
| 119m | process | process_availability_050 | above_T4 | above_T4 | T4 | T4 |
| 119m | process | process_availability_075 | above_T4 | above_T4 | above_T4 | above_T4 |
| 119m | harvest | harvest_recovery_035 | T4 | T4 | T3 | T3 |
| 119m | harvest | harvest_recovery_060 | above_T4 | above_T4 | T4 | T4 |
| 119m | harvest | harvest_recovery_075 | above_T4 | above_T4 | above_T4 | above_T4 |
| 150m | process | process_availability_000 | T1 | T1 | T1 | T1 |
| 150m | process | process_availability_025 | T4 | T4 | T3 | T3 |
| 150m | process | process_availability_050 | above_T4 | above_T4 | above_T4 | above_T4 |
| 150m | process | process_availability_075 | above_T4 | above_T4 | above_T4 | above_T4 |
| 150m | harvest | harvest_recovery_035 | T4 | T4 | T3 | T3 |
| 150m | harvest | harvest_recovery_060 | above_T4 | above_T4 | above_T4 | above_T4 |
| 150m | harvest | harvest_recovery_075 | above_T4 | above_T4 | above_T4 | above_T4 |

Frozen v5.1 reference positions: 21/21.
Operable primary/achieved matches: 100 Mm3
4/7 and 5/7;
119 Mm3 3/7 and
3/7; 150 Mm3
5/7 and
5/7.

## 4. Boundary

- The operable chains are share-based landbase proxies, not legal THLB.
- No slope or spatial road screen is applied.
- The official OSeCAN tree is unchanged (146 files, 80caa91c3e91c890..., changed_files=0).
- No chain v5.1, full-forest case, or UI artifact is changed.
