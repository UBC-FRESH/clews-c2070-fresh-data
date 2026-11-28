# Sustainable 119 Mm3 WS4 Forestry Residue Handoff to OSeCAN

**Artifact:** `forestry_osecan_handoff_ws4_sustainable` **Version:** 1.0.0

**Status:** pass. Built from the sustainable 100-year WS4 chain totals. The
official OSeCAN tree, handoff v10, residue curve v9 and frozen chain v5.1 are
unchanged.

**Labels:** `model_estimate=true`, `observed=false`, `policy_grade=false`,
`national_claim=false`, `ws4_derived=true`, `sustainable_schedule=true`,
`official_osecan_changed=false`, `chain_v51_unchanged=true`.

## 1. Source

- Chain: `data/derived/national/facilities/ws4_transformed_119m`
- Zone weights: frozen handoff v10 `zone_allocation_weights.csv`
- Tier thresholds: official OSeCAN `national_supply_curve/tier_definitions.csv`
- Process cases: 0%, 25%, 50%, 75% of process residue
- Harvest cases: 0.35, 0.60, 0.75 recovery

The sustainable WS4 chain is origin-province based. Handoff v10 process
residue is facility-province based, so zone rows are not compared directly
across the two bases; only national totals and tier positions are compared.

## 2. 119 Mm3 tier positions

| Basis | Stream | Case | National PJ | Tier | v10 PJ | v10 tier |
|---|---|---|---:|---|---:|---|
| sustainable_119m | process | process_availability_000 | 0.000000 | T1 | 0.000000 | T1 |
| sustainable_119m | process | process_availability_025 | 124.650482 | T3 | 124.687729 | T3 |
| sustainable_119m | process | process_availability_050 | 249.300963 | above_T4 | 249.375458 | above_T4 |
| sustainable_119m | process | process_availability_075 | 373.951445 | above_T4 | 374.063188 | above_T4 |
| sustainable_119m | harvest | harvest_recovery_035 | 156.042982 | T4 | 155.543768 | T4 |
| sustainable_119m | harvest | harvest_recovery_060 | 267.502254 | above_T4 | 266.646460 | above_T4 |
| sustainable_119m | harvest | harvest_recovery_075 | 334.377818 | above_T4 | 333.308075 | above_T4 |
| sustainable_achieved | process | process_availability_000 | 0.000000 | T1 | 0.000000 | T1 |
| sustainable_achieved | process | process_availability_025 | 125.780631 | T3 | 124.687729 | T3 |
| sustainable_achieved | process | process_availability_050 | 251.561262 | above_T4 | 249.375458 | above_T4 |
| sustainable_achieved | process | process_availability_075 | 377.341892 | above_T4 | 374.063188 | above_T4 |
| sustainable_achieved | harvest | harvest_recovery_035 | 157.457752 | T4 | 155.543768 | T4 |
| sustainable_achieved | harvest | harvest_recovery_060 | 269.927575 | above_T4 | 266.646460 | above_T4 |
| sustainable_achieved | harvest | harvest_recovery_075 | 337.409469 | above_T4 | 333.308075 | above_T4 |

## 3. Tier comparison

| Scenario | Stream | Case | Frozen v5.1 | v10 | Sustainable primary | Sustainable achieved |
|---|---|---|---|---|---|---|
| 100m | process | process_availability_000 | T1 | T1 | not_available | not_available |
| 100m | process | process_availability_025 | T2 | T2 | not_available | not_available |
| 100m | process | process_availability_050 | T4 | T4 | not_available | not_available |
| 100m | process | process_availability_075 | above_T4 | above_T4 | not_available | not_available |
| 100m | harvest | harvest_recovery_035 | T3 | T3 | not_available | not_available |
| 100m | harvest | harvest_recovery_060 | above_T4 | above_T4 | not_available | not_available |
| 100m | harvest | harvest_recovery_075 | above_T4 | above_T4 | not_available | not_available |
| 119m | process | process_availability_000 | T1 | T1 | T1 | T1 |
| 119m | process | process_availability_025 | T3 | T3 | T3 | T3 |
| 119m | process | process_availability_050 | above_T4 | above_T4 | above_T4 | above_T4 |
| 119m | process | process_availability_075 | above_T4 | above_T4 | above_T4 | above_T4 |
| 119m | harvest | harvest_recovery_035 | T4 | T4 | T4 | T4 |
| 119m | harvest | harvest_recovery_060 | above_T4 | above_T4 | above_T4 | above_T4 |
| 119m | harvest | harvest_recovery_075 | above_T4 | above_T4 | above_T4 | above_T4 |
| 150m | process | process_availability_000 | T1 | T1 | not_available | not_available |
| 150m | process | process_availability_025 | T4 | T4 | not_available | not_available |
| 150m | process | process_availability_050 | above_T4 | above_T4 | not_available | not_available |
| 150m | process | process_availability_075 | above_T4 | above_T4 | not_available | not_available |
| 150m | harvest | harvest_recovery_035 | T4 | T4 | not_available | not_available |
| 150m | harvest | harvest_recovery_060 | above_T4 | above_T4 | not_available | not_available |
| 150m | harvest | harvest_recovery_075 | above_T4 | above_T4 | not_available | not_available |

- Frozen v5.1 21/21 reference positions match handoff v10:
  `21/21`.
- Sustainable 119 Mm3 primary positions match v10:
  `7/7`.
- Sustainable 119 Mm3 achieved positions match v10:
  `7/7`.
- Official OSeCAN tree unchanged: `True`
  (146 files, 80caa91c3e91c890..., changed_files=0).

## 4. Caveats

- The sustainable WS4 chain is a whole-block model estimate, not an AAC,
  policy result, or investment case.
- Zone weights are frozen handoff-v10 screening proxies, not observed
  sub-provincial residue shares.
- Process and harvest residues remain separate streams; 0.60 harvest recovery
  is a reference case, not a calibrated factor.
- No official OSeCAN file, frozen v5.1 artifact, or candidate activity limit is
  changed.
