# Sustainable 150 Mm3/yr WS4 Schedule and Chain

**Artifact:** `ws4_transformed_natural_sustainable_150m` **Version:** 1.0.0

**Status:** pass. The 150,000,000.2 m3/yr case is sustained for 100 years. This is a whole-block model estimate, not an AAC, policy result, tenure plan, or investment case.

**Labels:** `model_estimate=true`, `observed=false`, `policy_grade=false`, `national_claim=false`, `ws4_derived=true`, `sustainable_schedule=true`, `transformed_curves=true`, `natural_5param_only=true`, `managed_basis_quarantined=true`, `official_osecan_changed=false`, `chain_v51_unchanged=true`.

## 1. Input and method

- Dataset: `data/derived/ws4/scanfi-national-990m-transformed-natural/dataset`
- Schedule: `data/derived/ws4/scanfi-national-990m-transformed-natural/sustainable-150m/schedule.csv`
- Run: `data/derived/ws4/scanfi-national-990m-transformed-natural/sustainable-150m/run_100y`
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
| 0 | 0-9 | 1500.000 | 1500.025 | 0.0017 | 8.383 | 39473 |
| 1 | 10-19 | 1500.000 | 1500.043 | 0.0029 | 7.645 | 22457 |
| 2 | 20-29 | 1500.000 | 1500.044 | 0.0029 | 7.359 | 19075 |
| 3 | 30-39 | 1500.000 | 1554.323 | 3.6215 | 7.857 | 25535 |
| 4 | 40-49 | 1500.000 | 1549.590 | 3.3060 | 7.691 | 23794 |
| 5 | 50-59 | 1500.000 | 1523.871 | 1.5914 | 7.444 | 25662 |
| 6 | 60-69 | 1500.000 | 1523.899 | 1.5933 | 6.473 | 33405 |
| 7 | 70-79 | 1500.000 | 1536.926 | 2.4617 | 6.325 | 21297 |
| 8 | 80-89 | 1500.000 | 1528.826 | 1.9218 | 6.591 | 16979 |
| 9 | 90-99 | 1500.000 | 1625.736 | 8.3824 | 6.613 | 17703 |

- Annual harvest minimum: 149,934,996.8 m3/yr.
- Annual harvest maximum: 162,573,632.3 m3/yr.
- Annual mean: 153,432,833.3 m3/yr.
- Annual CV: 0.023291.
- Annual floor met: `False`; gap to the nominal
  annual rate: 65,003.4 m3.
- Period shortfall: 0.0 m3.
- Sustained: `True`.
- Selected blocks: 245,380
  (72.380 Mha).
- Blocks reharvested within 100 years: 0.

## 3. Harvest by province

| Province | Control share | Target Mm3/yr | First period Mm3/yr | 100-year Mm3/yr | Area Mha | Blocks |
|---|---|---|---|---|---|---|
| BC | 30.149% | 45.223878 | 54.029748 | 47.361055 | 10.087 | 67565 |
| AB | 20.067% | 30.100000 | 30.709412 | 30.888340 | 10.839 | 31188 |
| SK | 4.307% | 6.460155 | 6.088265 | 6.614383 | 4.413 | 14738 |
| MB | 1.125% | 1.687988 | 1.742522 | 1.757761 | 1.282 | 2807 |
| ON | 13.376% | 20.063703 | 20.631307 | 22.186344 | 14.661 | 26495 |
| QC | 22.743% | 34.115200 | 34.643632 | 34.950318 | 25.931 | 81566 |
| NB | 4.156% | 6.234700 | 0.009575 | 4.445117 | 1.770 | 8801 |
| NS | 2.367% | 3.551095 | 0.000000 | 2.824175 | 1.325 | 2915 |
| PE | 0.300% | 0.449358 | 0.000000 | 0.247759 | 0.135 | 1018 |
| NL | 1.341% | 2.012233 | 2.043955 | 2.047751 | 1.862 | 7629 |
| YT | 0.044% | 0.065314 | 0.066872 | 0.067274 | 0.038 | 316 |
| NT | 0.024% | 0.036376 | 0.037214 | 0.042555 | 0.039 | 342 |
| NU | 0.000% | 0.000000 | 0.000000 | 0.000000 | 0.000 | 0 |

## 4. Chain versus frozen v5.1

| Metric | Unit | v5.1 | First-period basis | Delta % | Achieved basis | Delta % |
|---|---|---|---|---|---|---|
| harvest_m3 | m3 | 150000000.200000 | 150002502.201248 | 0.0017 | 153432833.321506 | 2.2886 |
| solid_product_m3 | m3 | 46136665.718213 | 47909896.107021 | 3.8434 | 47420956.097699 | 2.7837 |
| sawlog_product_m3 | m3 | 41585119.517419 | 43183414.420238 | 3.8434 | 42742710.082203 | 2.7837 |
| panel_product_m3 | m3 | 4551546.200794 | 4726481.686783 | 3.8434 | 4678246.015496 | 2.7837 |
| pulp_product_odt | odt | 15550881.011045 | 15016943.254881 | -3.4335 | 15824540.216214 | 1.7598 |
| pellet_product_odt | odt | 7038938.165569 | 6801673.127114 | -3.3708 | 7232257.248072 | 2.7464 |
| bio_product_mwh | MWh | 1253014.284904 | 1210778.300513 | -3.3708 | 1287427.369125 | 2.7464 |
| process_residue_m3 | m3 | 75299125.458469 | 75508189.985020 | 0.2776 | 77040044.619075 | 2.3120 |
| process_residue_odt | odt | 33884606.456311 | 33978685.493275 | 0.2776 | 34668020.078599 | 2.3120 |
| process_residue_pj | PJ | 626.865219 | 628.605682 | 0.2776 | 641.358371 | 2.3120 |
| harvest_residue_gross_odt | odt | 30979752.054305 | 30190147.027362 | -2.5488 | 31600907.561207 | 2.0050 |
| harvest_residue_gross_pj | PJ | 573.125413 | 558.517720 | -2.5488 | 584.616790 | 2.0050 |
| harvest_residue_recoverable_r035_odt | odt | 10842913.219007 | 10566551.459589 | -2.5488 | 11060317.646437 | 2.0050 |
| harvest_residue_recoverable_r035_pj | PJ | 200.593895 | 195.481202 | -2.5488 | 204.615876 | 2.0050 |
| harvest_residue_recoverable_r060_odt | odt | 18587851.232583 | 18114088.216433 | -2.5488 | 18960544.536739 | 2.0050 |
| harvest_residue_recoverable_r060_pj | PJ | 343.875248 | 335.110632 | -2.5488 | 350.770074 | 2.0050 |
| harvest_residue_recoverable_r075_odt | odt | 23234814.040728 | 22642610.270554 | -2.5488 | 23700680.670937 | 2.0050 |
| harvest_residue_recoverable_r075_pj | PJ | 429.844060 | 418.888290 | -2.5488 | 438.462592 | 2.0050 |
| total_residue_gross_pj | PJ | 1199.990632 | 1187.123402 | -1.0723 | 1225.975161 | 2.1654 |
| total_residue_recoverable_r035_pj | PJ | 827.459114 | 824.086884 | -0.4075 | 845.974248 | 2.2376 |
| total_residue_recoverable_r060_pj | PJ | 970.740467 | 963.716314 | -0.7236 | 992.128445 | 2.2033 |
| total_residue_recoverable_r075_pj | PJ | 1056.709279 | 1047.493972 | -0.8721 | 1079.820964 | 2.1871 |

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
