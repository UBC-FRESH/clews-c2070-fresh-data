# Sustainable 150 Mm3/yr WS4 Schedule and Chain

**Artifact:** `ws4_sustainable_150m` **Version:** 1.0.0

**Status:** pass. The 150,000,000.2 m3/yr case is sustained for 100 years. This is a whole-block model estimate, not an AAC, policy result, tenure plan, or investment case.

**Labels:** `model_estimate=true`, `observed=false`, `policy_grade=false`,
`national_claim=false`, `ws4_derived=true`, `sustainable_schedule=true`,
`official_osecan_changed=false`, `chain_v51_unchanged=true`.

## 1. Input and method

- Dataset: `data/derived/ws4/scanfi-national-990m/dataset`
- Schedule: `data/derived/ws4/sustainable-150m/schedule.csv`
- Run: `data/derived/ws4/sustainable-150m/run_100y`
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
| 0 | 0-9 | 1500.000 | 1533.711 | 2.2474 | 12.249 | 52088 |
| 1 | 10-19 | 1500.000 | 1503.694 | 0.2462 | 10.737 | 28332 |
| 2 | 20-29 | 1500.000 | 1518.321 | 1.2214 | 10.899 | 38169 |
| 3 | 30-39 | 1500.000 | 1504.540 | 0.3027 | 11.248 | 36750 |
| 4 | 40-49 | 1500.000 | 1501.156 | 0.0771 | 10.322 | 53420 |
| 5 | 50-59 | 1500.000 | 1526.450 | 1.7633 | 10.366 | 31624 |
| 6 | 60-69 | 1500.000 | 1526.089 | 1.7393 | 10.770 | 29024 |
| 7 | 70-79 | 1500.000 | 1506.302 | 0.4201 | 9.943 | 43881 |
| 8 | 80-89 | 1500.000 | 1501.852 | 0.1235 | 10.310 | 44846 |
| 9 | 90-99 | 1500.000 | 1502.653 | 0.1769 | 9.734 | 41915 |

- Annual harvest minimum: 149,997,027.4 m3/yr.
- Annual harvest maximum: 153,495,684.4 m3/yr.
- Annual mean: 151,247,672.3 m3/yr.
- Annual CV: 0.008033.
- Annual floor met: `False`; gap to the nominal
  annual rate: 2,972.8 m3.
- Period shortfall: 0.0 m3.
- Sustained: `True`.
- Selected blocks: 400,049
  (106.577 Mha).
- Blocks reharvested within 100 years: 586.

## 3. Harvest by province

| Province | Control share | Target Mm3/yr | First period Mm3/yr | 100-year Mm3/yr | Area Mha | Blocks |
|---|---|---|---|---|---|---|
| BC | 30.149% | 45.223878 | 45.572534 | 45.261662 | 18.821 | 131150 |
| AB | 20.067% | 30.100000 | 30.115392 | 30.198326 | 16.452 | 48282 |
| SK | 4.307% | 6.460155 | 6.470920 | 6.473863 | 6.053 | 24049 |
| MB | 1.125% | 1.687988 | 1.748411 | 1.784902 | 2.010 | 3288 |
| ON | 13.376% | 20.063703 | 20.076442 | 20.328842 | 18.325 | 41980 |
| QC | 22.743% | 34.115200 | 34.115452 | 34.289238 | 35.081 | 112478 |
| NB | 4.156% | 6.234700 | 6.266576 | 6.251245 | 3.498 | 15941 |
| NS | 2.367% | 3.551095 | 6.429631 | 4.043474 | 2.832 | 9535 |
| PE | 0.300% | 0.449358 | 0.457259 | 0.459572 | 0.347 | 3058 |
| NL | 1.341% | 2.012233 | 2.014008 | 2.050867 | 3.037 | 9215 |
| YT | 0.044% | 0.065314 | 0.065930 | 0.066533 | 0.070 | 548 |
| NT | 0.024% | 0.036376 | 0.038520 | 0.039149 | 0.052 | 525 |
| NU | 0.000% | 0.000000 | 0.000000 | 0.000000 | 0.000 | 0 |

## 4. Chain versus frozen v5.1

| Metric | Unit | v5.1 | First-period basis | Delta % | Achieved basis | Delta % |
|---|---|---|---|---|---|---|
| harvest_m3 | m3 | 150000000.200000 | 153371076.210678 | 2.2474 | 151247672.316712 | 0.8318 |
| solid_product_m3 | m3 | 46136665.718213 | 46741639.058194 | 1.3113 | 46414539.794365 | 0.6023 |
| sawlog_product_m3 | m3 | 41585119.517419 | 42130410.085264 | 1.3113 | 41835580.327442 | 0.6023 |
| panel_product_m3 | m3 | 4551546.200794 | 4611228.972930 | 1.3113 | 4578959.466923 | 0.6023 |
| pulp_product_odt | odt | 15550881.011045 | 16047204.683579 | 3.1916 | 15715281.869293 | 1.0572 |
| pellet_product_odt | odt | 7038938.165569 | 7278829.165467 | 3.4081 | 7116045.098526 | 1.0954 |
| bio_product_mwh | MWh | 1253014.284904 | 1295717.721505 | 3.4081 | 1266740.231373 | 1.0954 |
| process_residue_m3 | m3 | 75299125.458469 | 76985683.771974 | 2.2398 | 75921462.288456 | 0.8265 |
| process_residue_odt | odt | 33884606.456311 | 34643557.697401 | 2.2398 | 34164658.029820 | 0.8265 |
| process_residue_pj | PJ | 626.865219 | 640.905817 | 2.2398 | 632.046174 | 0.8265 |
| harvest_residue_gross_odt | odt | 30979752.054305 | 31922013.026388 | 3.0415 | 31283479.159974 | 0.9804 |
| harvest_residue_gross_pj | PJ | 573.125413 | 590.557241 | 3.0415 | 578.744364 | 0.9804 |
| harvest_residue_recoverable_r035_odt | odt | 10842913.219007 | 11172704.559250 | 3.0415 | 10949217.706005 | 0.9804 |
| harvest_residue_recoverable_r035_pj | PJ | 200.593895 | 206.695034 | 3.0415 | 202.560528 | 0.9804 |
| harvest_residue_recoverable_r060_odt | odt | 18587851.232583 | 19153207.815846 | 3.0415 | 18770087.495998 | 0.9804 |
| harvest_residue_recoverable_r060_pj | PJ | 343.875248 | 354.334345 | 3.0415 | 347.246619 | 0.9804 |
| harvest_residue_recoverable_r075_odt | odt | 23234814.040728 | 23941509.769821 | 3.0415 | 23462609.370011 | 0.9804 |
| harvest_residue_recoverable_r075_pj | PJ | 429.844060 | 442.917931 | 3.0415 | 434.058273 | 0.9804 |
| total_residue_gross_pj | PJ | 1199.990632 | 1231.463058 | 2.6227 | 1210.790538 | 0.9000 |
| total_residue_recoverable_r035_pj | PJ | 827.459114 | 847.600852 | 2.4342 | 834.606701 | 0.8638 |
| total_residue_recoverable_r060_pj | PJ | 970.740467 | 995.240162 | 2.5238 | 979.292792 | 0.8810 |
| total_residue_recoverable_r075_pj | PJ | 1056.709279 | 1083.823748 | 2.5659 | 1066.104447 | 0.8891 |

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
