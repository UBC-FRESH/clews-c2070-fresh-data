# Sustainable 100/150 Mm3 WS4 Forestry Residue Handoff to OSeCAN

**Artifact:** `forestry_osecan_handoff_ws4_sustainable_cases` **Version:** 1.0.0

**Status:** pass. Built from the sustainable 100-year WS4 case
chains. The official OSeCAN tree, handoff v10, residue curve v9, chain v5.1,
and the 119 Mm3 case artifacts are unchanged.

**Labels:** `model_estimate=true`, `observed=false`, `policy_grade=false`,
`national_claim=false`, `ws4_derived=true`, `sustainable_schedule=true`,
`transformed_curves=true`, `official_osecan_changed=false`,
`chain_v51_unchanged=true`.

## 1. Source

- Case chains: `data/derived/national/facilities/ws4_transformed_cases/sustainable/100m` and
  `data/derived/national/facilities/ws4_transformed_cases/sustainable/150m`
- Zone weights: frozen handoff v10 `zone_allocation_weights.csv`
- Tier thresholds: official OSeCAN `national_supply_curve/tier_definitions.csv`
- Process cases: 0%, 25%, 50%, 75% of process residue
- Harvest cases: 0.35, 0.60, 0.75 recovery

The sustainable WS4 chains are origin-province based. Handoff v10 process
residue is facility-province based, so zone rows are not compared directly
across the two bases; only national totals and tier positions are compared.

## 2. Tier positions

| Case | Basis | Stream | Case | National PJ | Tier | v10 PJ | v10 tier |
|---|---|---|---|---:|---|---:|---|
| 100m | sustainable_100m | process | process_availability_000 | 0.000000 | T1 | 0.000000 | T1 |
| 100m | sustainable_100m | process | process_availability_025 | 105.523334 | T2 | 104.809505 | T2 |
| 100m | sustainable_100m | process | process_availability_050 | 211.046667 | T4 | 209.619009 | T4 |
| 100m | sustainable_100m | process | process_availability_075 | 316.570001 | above_T4 | 314.428514 | above_T4 |
| 100m | sustainable_100m | harvest | harvest_recovery_035 | 131.836011 | T3 | 130.635373 | T3 |
| 100m | sustainable_100m | harvest | harvest_recovery_060 | 226.004590 | above_T4 | 223.946354 | above_T4 |
| 100m | sustainable_100m | harvest | harvest_recovery_075 | 282.505738 | above_T4 | 279.932942 | above_T4 |
| 100m | sustainable_achieved | process | process_availability_000 | 0.000000 | T1 | 0.000000 | T1 |
| 100m | sustainable_achieved | process | process_availability_025 | 105.949344 | T2 | 104.809505 | T2 |
| 100m | sustainable_achieved | process | process_availability_050 | 211.898688 | T4 | 209.619009 | T4 |
| 100m | sustainable_achieved | process | process_availability_075 | 317.848032 | above_T4 | 314.428514 | above_T4 |
| 100m | sustainable_achieved | harvest | harvest_recovery_035 | 132.596737 | T3 | 130.635373 | T3 |
| 100m | sustainable_achieved | harvest | harvest_recovery_060 | 227.308693 | above_T4 | 223.946354 | above_T4 |
| 100m | sustainable_achieved | harvest | harvest_recovery_075 | 284.135866 | above_T4 | 279.932942 | above_T4 |
| 150m | sustainable_150m | process | process_availability_000 | 0.000000 | T1 | 0.000000 | T1 |
| 150m | sustainable_150m | process | process_availability_025 | 160.623631 | T4 | 156.716305 | T4 |
| 150m | sustainable_150m | process | process_availability_050 | 321.247261 | above_T4 | 313.432610 | above_T4 |
| 150m | sustainable_150m | process | process_availability_075 | 481.870892 | above_T4 | 470.148915 | above_T4 |
| 150m | sustainable_150m | harvest | harvest_recovery_035 | 207.655046 | T4 | 200.593895 | T4 |
| 150m | sustainable_150m | harvest | harvest_recovery_060 | 355.980079 | above_T4 | 343.875248 | above_T4 |
| 150m | sustainable_150m | harvest | harvest_recovery_075 | 444.975098 | above_T4 | 429.844060 | above_T4 |
| 150m | sustainable_achieved | process | process_availability_000 | 0.000000 | T1 | 0.000000 | T1 |
| 150m | sustainable_achieved | process | process_availability_025 | 158.399666 | T4 | 156.716305 | T4 |
| 150m | sustainable_achieved | process | process_availability_050 | 316.799331 | above_T4 | 313.432610 | above_T4 |
| 150m | sustainable_achieved | process | process_availability_075 | 475.198997 | above_T4 | 470.148915 | above_T4 |
| 150m | sustainable_achieved | harvest | harvest_recovery_035 | 203.155481 | T4 | 200.593895 | T4 |
| 150m | sustainable_achieved | harvest | harvest_recovery_060 | 348.266539 | above_T4 | 343.875248 | above_T4 |
| 150m | sustainable_achieved | harvest | harvest_recovery_075 | 435.333174 | above_T4 | 429.844060 | above_T4 |

## 3. Tier comparison

| Scenario | Stream | Case | Frozen v5.1 | v10 | WS4 primary | WS4 achieved |
|---|---|---|---|---|---|---|
| 100m | process | process_availability_000 | T1 | T1 | T1 | T1 |
| 100m | process | process_availability_025 | T2 | T2 | T2 | T2 |
| 100m | process | process_availability_050 | T4 | T4 | T4 | T4 |
| 100m | process | process_availability_075 | above_T4 | above_T4 | above_T4 | above_T4 |
| 100m | harvest | harvest_recovery_035 | T3 | T3 | T3 | T3 |
| 100m | harvest | harvest_recovery_060 | above_T4 | above_T4 | above_T4 | above_T4 |
| 100m | harvest | harvest_recovery_075 | above_T4 | above_T4 | above_T4 | above_T4 |
| 119m | process | process_availability_000 | T1 | T1 | not_available | not_available |
| 119m | process | process_availability_025 | T3 | T3 | not_available | not_available |
| 119m | process | process_availability_050 | above_T4 | above_T4 | not_available | not_available |
| 119m | process | process_availability_075 | above_T4 | above_T4 | not_available | not_available |
| 119m | harvest | harvest_recovery_035 | T4 | T4 | not_available | not_available |
| 119m | harvest | harvest_recovery_060 | above_T4 | above_T4 | not_available | not_available |
| 119m | harvest | harvest_recovery_075 | above_T4 | above_T4 | not_available | not_available |
| 150m | process | process_availability_000 | T1 | T1 | T1 | T1 |
| 150m | process | process_availability_025 | T4 | T4 | T4 | T4 |
| 150m | process | process_availability_050 | above_T4 | above_T4 | above_T4 | above_T4 |
| 150m | process | process_availability_075 | above_T4 | above_T4 | above_T4 | above_T4 |
| 150m | harvest | harvest_recovery_035 | T4 | T4 | T4 | T4 |
| 150m | harvest | harvest_recovery_060 | above_T4 | above_T4 | above_T4 | above_T4 |
| 150m | harvest | harvest_recovery_075 | above_T4 | above_T4 | above_T4 | above_T4 |

- Frozen v5.1 21/21 reference positions match handoff v10:
  `21/21`.
- 100 Mm3 primary/achieved positions match:
  `7/7`,
  `7/7`.
- 150 Mm3 primary/achieved positions match:
  `7/7`,
  `7/7`.
- Official OSeCAN tree unchanged: `True`
  (146 files, 80caa91c3e91c890..., changed_files=0).

## 4. Caveats

- The sustainable WS4 chains are whole-block model estimates, not AACs,
  policy results, or investment cases.
- Zone weights are frozen handoff-v10 screening proxies, not observed
  sub-provincial residue shares.
- Process and harvest residues remain separate streams; 0.60 harvest recovery
  is a reference case, not a calibrated factor.
- No official OSeCAN file, frozen v5.1 artifact, or candidate activity limit is
  changed.
