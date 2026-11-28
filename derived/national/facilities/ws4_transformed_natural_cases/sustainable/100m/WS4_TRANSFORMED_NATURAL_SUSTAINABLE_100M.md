# Sustainable 100 Mm3/yr WS4 Schedule and Chain

**Artifact:** `ws4_transformed_natural_sustainable_100m` **Version:** 1.0.0

**Status:** pass. The 100,000,000.1 m3/yr case is sustained for 100 years. This is a whole-block model estimate, not an AAC, policy result, tenure plan, or investment case.

**Labels:** `model_estimate=true`, `observed=false`, `policy_grade=false`, `national_claim=false`, `ws4_derived=true`, `sustainable_schedule=true`, `transformed_curves=true`, `natural_5param_only=true`, `managed_basis_quarantined=true`, `official_osecan_changed=false`, `chain_v51_unchanged=true`.

## 1. Input and method

- Dataset: `data/derived/ws4/scanfi-national-990m-transformed-natural/dataset`
- Schedule: `data/derived/ws4/scanfi-national-990m-transformed-natural/sustainable-100m/schedule.csv`
- Run: `data/derived/ws4/scanfi-national-990m-transformed-natural/sustainable-100m/run_100y`
- Control: `data/derived/national/harvest_basis/provincial_allocation/100m.csv`
- Horizon: 100 years, 10 periods of 10 years.
- Period target: 1,000,000,001.0 m3.
- Selection: whole blocks, oldest-first, volume-aware, within provincial
  period targets from the frozen 100m allocated shares; no block is
  split, scaled, or harvested below rotation.
- Annual assignment: longest-processing-time balancing of exact annual
  volumes over the ten offsets of each period.

## 2. Period harvest

| Period | Offsets | Target Mm3 | Achieved Mm3 | Overshoot % | Area Mha | Blocks |
|---|---|---|---|---|---|---|
| 0 | 0-9 | 1000.000 | 1000.060 | 0.0060 | 5.295 | 27121 |
| 1 | 10-19 | 1000.000 | 1000.037 | 0.0037 | 4.987 | 18870 |
| 2 | 20-29 | 1000.000 | 1000.023 | 0.0023 | 4.699 | 15715 |
| 3 | 30-39 | 1000.000 | 1004.347 | 0.4347 | 4.629 | 9667 |
| 4 | 40-49 | 1000.000 | 1014.051 | 1.4051 | 4.545 | 10971 |
| 5 | 50-59 | 1000.000 | 1040.241 | 4.0241 | 4.630 | 23297 |
| 6 | 60-69 | 1000.000 | 1021.017 | 2.1017 | 4.479 | 11733 |
| 7 | 70-79 | 1000.000 | 1067.019 | 6.7019 | 4.724 | 16773 |
| 8 | 80-89 | 1000.000 | 1010.888 | 1.0888 | 4.465 | 16536 |
| 9 | 90-99 | 1000.000 | 1009.018 | 0.9018 | 4.358 | 13456 |

- Annual harvest minimum: 99,784,999.3 m3/yr.
- Annual harvest maximum: 106,701,857.0 m3/yr.
- Annual mean: 101,667,010.4 m3/yr.
- Annual CV: 0.020148.
- Annual floor met: `False`; gap to the nominal
  annual rate: 215,000.8 m3.
- Period shortfall: 0.0 m3.
- Sustained: `True`.
- Selected blocks: 164,139
  (46.813 Mha).
- Blocks reharvested within 100 years: 0.

## 3. Harvest by province

| Province | Control share | Target Mm3/yr | First period Mm3/yr | 100-year Mm3/yr | Area Mha | Blocks |
|---|---|---|---|---|---|---|
| BC | 33.249% | 33.248823 | 40.413862 | 35.061260 | 7.215 | 46419 |
| AB | 19.038% | 19.038002 | 19.362402 | 19.394461 | 5.953 | 20666 |
| SK | 3.613% | 3.613337 | 3.736503 | 3.891791 | 2.578 | 6960 |
| MB | 0.944% | 0.944137 | 0.971096 | 1.067704 | 0.729 | 1083 |
| ON | 11.222% | 11.222165 | 11.765257 | 12.048275 | 8.485 | 14375 |
| QC | 22.184% | 22.184137 | 22.414700 | 22.627022 | 18.080 | 58105 |
| NB | 6.235% | 6.234700 | 0.009650 | 4.445472 | 1.770 | 8801 |
| NS | 1.986% | 1.986222 | 0.000000 | 1.684039 | 0.772 | 1622 |
| PE | 0.251% | 0.251338 | 0.000000 | 0.145225 | 0.080 | 595 |
| NL | 1.209% | 1.209274 | 1.260913 | 1.229969 | 1.099 | 5046 |
| YT | 0.037% | 0.036532 | 0.039808 | 0.038061 | 0.022 | 184 |
| NT | 0.031% | 0.031333 | 0.031835 | 0.033731 | 0.030 | 283 |
| NU | 0.000% | 0.000000 | 0.000000 | 0.000000 | 0.000 | 0 |

## 4. Chain versus frozen v5.1

| Metric | Unit | v5.1 | First-period basis | Delta % | Achieved basis | Delta % |
|---|---|---|---|---|---|---|
| harvest_m3 | m3 | 100000000.100000 | 100006025.448605 | 0.0060 | 101667010.420846 | 1.6670 |
| solid_product_m3 | m3 | 31692807.151334 | 32822684.951997 | 3.5651 | 32324084.503968 | 1.9919 |
| sawlog_product_m3 | m3 | 28566198.981094 | 29584610.317268 | 3.5651 | 29135198.577170 | 1.9919 |
| panel_product_m3 | m3 | 3126608.170239 | 3238074.634729 | 3.5651 | 3188885.926798 | 1.9919 |
| pulp_product_odt | odt | 10136702.863917 | 9769891.609953 | -3.6186 | 10253207.317882 | 1.1493 |
| pellet_product_odt | odt | 4372287.851260 | 4364650.233018 | -0.1747 | 4532129.013806 | 3.6558 |
| bio_product_mwh | MWh | 778318.974606 | 776959.388183 | -0.1747 | 806772.592932 | 3.6558 |
| process_residue_m3 | m3 | 50358921.112605 | 50480170.662514 | 0.2408 | 51195893.581644 | 1.6620 |
| process_residue_odt | odt | 22661514.500672 | 22716076.798143 | 0.2408 | 23038152.111752 | 1.6620 |
| process_residue_pj | PJ | 419.238018 | 420.247421 | 0.2408 | 426.205814 | 1.6620 |
| harvest_residue_gross_odt | odt | 20175347.205464 | 19829883.832261 | -1.7123 | 20551157.357162 | 1.8627 |
| harvest_residue_gross_pj | PJ | 373.243923 | 366.852851 | -1.7123 | 380.196411 | 1.8627 |
| harvest_residue_recoverable_r035_odt | odt | 7061371.521912 | 6940459.341298 | -1.7123 | 7192905.075014 | 1.8627 |
| harvest_residue_recoverable_r035_pj | PJ | 130.635373 | 128.398498 | -1.7123 | 133.068744 | 1.8627 |
| harvest_residue_recoverable_r060_odt | odt | 12105208.323278 | 11897930.299367 | -1.7123 | 12330694.414306 | 1.8627 |
| harvest_residue_recoverable_r060_pj | PJ | 223.946354 | 220.111711 | -1.7123 | 228.117847 | 1.8627 |
| harvest_residue_recoverable_r075_odt | odt | 15131510.404098 | 14872412.874217 | -1.7123 | 15413368.017891 | 1.8627 |
| harvest_residue_recoverable_r075_pj | PJ | 279.932942 | 275.139638 | -1.7123 | 285.147308 | 1.8627 |
| total_residue_gross_pj | PJ | 792.481942 | 787.100272 | -0.6791 | 806.402225 | 1.7565 |
| total_residue_recoverable_r035_pj | PJ | 549.873391 | 548.645919 | -0.2232 | 559.274558 | 1.7097 |
| total_residue_recoverable_r060_pj | PJ | 643.184372 | 640.359131 | -0.4393 | 654.323661 | 1.7319 |
| total_residue_recoverable_r075_pj | PJ | 699.170961 | 695.387059 | -0.5412 | 711.353122 | 1.7424 |

The first-period basis applies the frozen v5.1 per-province coefficients to
the annual average of offsets 0-9. The achieved basis applies them to the
100-year annual average. The comparison values are the frozen 100/150 Mm3
targets in `data/derived/national/facilities/national_facility_chain_scenarios_v9/scenario_summary.csv`, guarded against the model-card
values.

## 5. OSeCAN handoff

The combined `osecan/` artifact applies the existing WS4 origin-province
handoff logic to this chain. It verifies 21/21 frozen v5.1 reference positions
across the three scenarios, 7/7 tier positions for this case on both bases,
and an unchanged official OSeCAN tree.

## 6. Caveats

- The schedule is a national even-flow arithmetic model, not an AAC, policy result, tenure plan, or investment case.
- The full forest estate is used; no operability, tenure, road, slope, or mill-capacity screen is applied.
- Provincial period targets use the frozen 100m allocated_share values. A final whole block may overshoot a provincial target because no block is split or scaled.
- Rotation is the integer age of maximum MAI on the RSYC yield curve, capped to 40-200 years; the raw peak is flagged.
- Frozen chain v5.1 coefficients are applied to WS4 harvest by origin province. Facility assignment, mill capacity, transport, and interprovincial trade are not re-run.
- The primary chain basis uses the first-period annual average; the secondary basis uses the 100-year achieved average. Neither is an official OSeCAN change.
