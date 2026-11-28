# Sustainable 150 Mm3/yr WS4 Schedule and Chain

**Artifact:** `ws4_transformed_sustainable_150m` **Version:** 1.0.0

**Status:** pass. The 150,000,000.2 m3/yr case is sustained for 100 years. This is a whole-block model estimate, not an AAC, policy result, tenure plan, or investment case.

**Labels:** `model_estimate=true`, `observed=false`, `policy_grade=false`,
`national_claim=false`, `ws4_derived=true`, `sustainable_schedule=true`,
`transformed_curves=true`, `official_osecan_changed=false`,
`chain_v51_unchanged=true`.

## 1. Input and method

- Dataset: `data/derived/ws4/scanfi-national-990m-transformed/dataset`
- Schedule: `data/derived/ws4/scanfi-national-990m-transformed/sustainable-150m/schedule.csv`
- Run: `data/derived/ws4/scanfi-national-990m-transformed/sustainable-150m/run_100y`
- Control: `data/derived/national/harvest_basis/provincial_allocation/150m.csv`
- Horizon: 100 years, 10 periods of 10 years.
- Period target: 1,500,000,002.0 m3.
- Selection: whole blocks, oldest-first, volume-aware, within provincial
  period targets from the frozen 150m allocated shares; no block is
  split, scaled, or harvested below rotation.
- Annual assignment: longest-processing-time balancing of exact annual
  volumes over the ten offsets of each period.

## 2. Period harvest

| Period | Offsets | Target Mm3 | Achieved Mm3 | Overshoot % | Area Mha | Blocks |
|---|---|---|---|---|---|---|
| 0 | 0-9 | 1500.000 | 1538.005 | 2.5336 | 11.049 | 45883 |
| 1 | 10-19 | 1500.000 | 1509.875 | 0.6583 | 9.688 | 23723 |
| 2 | 20-29 | 1500.000 | 1530.959 | 2.0639 | 9.935 | 30511 |
| 3 | 30-39 | 1500.000 | 1508.066 | 0.5377 | 10.020 | 30973 |
| 4 | 40-49 | 1500.000 | 1505.393 | 0.3595 | 9.098 | 38862 |
| 5 | 50-59 | 1500.000 | 1516.533 | 1.1022 | 8.704 | 27705 |
| 6 | 60-69 | 1500.000 | 1532.425 | 2.1617 | 9.276 | 22468 |
| 7 | 70-79 | 1500.000 | 1511.081 | 0.7387 | 8.498 | 36086 |
| 8 | 80-89 | 1500.000 | 1506.014 | 0.4009 | 8.733 | 25356 |
| 9 | 90-99 | 1500.000 | 1505.670 | 0.3780 | 8.149 | 32295 |

- Annual harvest minimum: 150,539,287.5 m3/yr.
- Annual harvest maximum: 153,800,475.8 m3/yr.
- Annual mean: 151,640,202.8 m3/yr.
- Annual CV: 0.007858.
- Annual floor met: `True`; gap to the nominal
  annual rate: 0.0 m3.
- Period shortfall: 0.0 m3.
- Sustained: `True`.
- Selected blocks: 313,862
  (93.151 Mha).
- Blocks reharvested within 100 years: 541.

## 3. Harvest by province

| Province | Control share | Target Mm3/yr | First period Mm3/yr | 100-year Mm3/yr | Area Mha | Blocks |
|---|---|---|---|---|---|---|
| BC | 30.149% | 45.223878 | 45.241223 | 45.250712 | 9.586 | 64089 |
| AB | 20.067% | 30.100000 | 30.644891 | 30.644746 | 13.280 | 36739 |
| SK | 4.307% | 6.460155 | 6.607105 | 6.554472 | 5.051 | 17018 |
| MB | 1.125% | 1.687988 | 1.738021 | 1.877947 | 1.886 | 3239 |
| ON | 13.376% | 20.063703 | 20.075771 | 20.214750 | 18.303 | 41749 |
| QC | 22.743% | 34.115200 | 34.138931 | 34.207248 | 35.245 | 112591 |
| NB | 4.156% | 6.234700 | 6.241909 | 6.245190 | 3.516 | 15958 |
| NS | 2.367% | 3.551095 | 6.545599 | 4.036523 | 2.837 | 9596 |
| PE | 0.300% | 0.449358 | 0.449409 | 0.452701 | 0.337 | 3013 |
| NL | 1.341% | 2.012233 | 2.013433 | 2.046103 | 3.034 | 9212 |
| YT | 0.044% | 0.065314 | 0.066872 | 0.067274 | 0.038 | 316 |
| NT | 0.024% | 0.036376 | 0.037309 | 0.042538 | 0.039 | 342 |
| NU | 0.000% | 0.000000 | 0.000000 | 0.000000 | 0.000 | 0 |

## 4. Chain versus frozen v5.1

| Metric | Unit | v5.1 | First-period basis | Delta % | Achieved basis | Delta % |
|---|---|---|---|---|---|---|
| harvest_m3 | m3 | 150000000.200000 | 153800473.489748 | 2.5336 | 151640202.795479 | 1.0935 |
| solid_product_m3 | m3 | 46136665.718213 | 46740796.879038 | 1.3094 | 46496333.428212 | 0.7796 |
| sawlog_product_m3 | m3 | 41585119.517419 | 42129650.990077 | 1.3094 | 41909304.728336 | 0.7796 |
| panel_product_m3 | m3 | 4551546.200794 | 4611145.888961 | 1.3094 | 4587028.699876 | 0.7796 |
| pulp_product_odt | odt | 15550881.011045 | 16125857.615050 | 3.6974 | 15764755.001192 | 1.3753 |
| pellet_product_odt | odt | 7038938.165569 | 7329072.207203 | 4.1218 | 7141454.324005 | 1.4564 |
| bio_product_mwh | MWh | 1253014.284904 | 1304661.577457 | 4.1218 | 1271263.374174 | 1.4564 |
| process_residue_m3 | m3 | 75299125.458469 | 77176519.247838 | 2.4932 | 76107947.501249 | 1.0741 |
| process_residue_odt | odt | 33884606.456311 | 34729433.661540 | 2.4932 | 34248576.375577 | 1.0741 |
| process_residue_pj | PJ | 626.865219 | 642.494523 | 2.4932 | 633.598663 | 1.0741 |
| harvest_residue_gross_odt | odt | 30979752.054305 | 32070277.344328 | 3.5201 | 31375363.865521 | 1.2770 |
| harvest_residue_gross_pj | PJ | 573.125413 | 593.300131 | 3.5201 | 580.444232 | 1.2770 |
| harvest_residue_recoverable_r035_odt | odt | 10842913.219007 | 11224597.070529 | 3.5201 | 10981377.352946 | 1.2770 |
| harvest_residue_recoverable_r035_pj | PJ | 200.593895 | 207.655046 | 3.5201 | 203.155481 | 1.2770 |
| harvest_residue_recoverable_r060_odt | odt | 18587851.232583 | 19242166.406610 | 3.5201 | 18825218.319326 | 1.2770 |
| harvest_residue_recoverable_r060_pj | PJ | 343.875248 | 355.980079 | 3.5201 | 348.266539 | 1.2770 |
| harvest_residue_recoverable_r075_odt | odt | 23234814.040728 | 24052708.008276 | 3.5201 | 23531522.899171 | 1.2770 |
| harvest_residue_recoverable_r075_pj | PJ | 429.844060 | 444.975098 | 3.5201 | 435.333174 | 1.2770 |
| total_residue_gross_pj | PJ | 1199.990632 | 1235.794654 | 2.9837 | 1214.042894 | 1.1710 |
| total_residue_recoverable_r035_pj | PJ | 827.459114 | 850.149569 | 2.7422 | 836.754144 | 1.1233 |
| total_residue_recoverable_r060_pj | PJ | 970.740467 | 998.474601 | 2.8570 | 981.865202 | 1.1460 |
| total_residue_recoverable_r075_pj | PJ | 1056.709279 | 1087.469621 | 2.9110 | 1068.931837 | 1.1567 |

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
- Provincial period targets use the frozen 150m allocated_share values. A final whole block may overshoot a provincial target because no block is split or scaled.
- Rotation is the integer age of maximum MAI on the RSYC yield curve, capped to 40-200 years; the raw peak is flagged.
- Frozen chain v5.1 coefficients are applied to WS4 harvest by origin province. Facility assignment, mill capacity, transport, and interprovincial trade are not re-run.
- The primary chain basis uses the first-period annual average; the secondary basis uses the 100-year achieved average. Neither is an official OSeCAN change.
