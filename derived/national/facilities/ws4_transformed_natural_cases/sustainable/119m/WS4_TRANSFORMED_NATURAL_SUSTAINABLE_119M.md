# Sustainable 119 Mm3/yr WS4 Schedule and Chain

**Artifact:** `ws4_transformed_natural_sustainable_119m` **Version:** 1.0.0

**Status:** pass. The 118,977,339.1 m3/yr case is sustained for 100 years. This is a whole-block model estimate, not an AAC, policy result, tenure plan, or investment case.

**Labels:** `model_estimate=true`, `observed=false`, `policy_grade=false`, `national_claim=false`, `ws4_derived=true`, `sustainable_schedule=true`, `transformed_curves=true`, `natural_5param_only=true`, `managed_basis_quarantined=true`, `official_osecan_changed=false`, `chain_v51_unchanged=true`.

## 1. Input and method

- Dataset: `data/derived/ws4/scanfi-national-990m-transformed-natural/dataset`
- Schedule: `data/derived/ws4/scanfi-national-990m-transformed-natural/sustainable-119m/schedule.csv`
- Run: `data/derived/ws4/scanfi-national-990m-transformed-natural/sustainable-119m/run_100y`
- Control: `data/derived/national/harvest_basis/provincial_allocation/119m.csv`
- Horizon: 100 years, 10 periods of 10 years.
- Period target: 1,189,773,391.0 m3.
- Selection: whole blocks, oldest-first, volume-aware, within provincial
  period targets from the frozen 119m allocated shares; no block is
  split, scaled, or harvested below rotation.
- Annual assignment: longest-processing-time balancing of exact annual
  volumes over the ten offsets of each period.

## 2. Period harvest

| Period | Offsets | Target Mm3 | Achieved Mm3 | Overshoot % | Area Mha | Blocks |
|---|---|---|---|---|---|---|
| 0 | 0-9 | 1189.773 | 1189.867 | 0.0078 | 6.481 | 32356 |
| 1 | 10-19 | 1189.773 | 1189.940 | 0.0140 | 5.698 | 19098 |
| 2 | 20-29 | 1189.773 | 1189.789 | 0.0013 | 5.553 | 15477 |
| 3 | 30-39 | 1189.773 | 1190.532 | 0.0638 | 5.541 | 12531 |
| 4 | 40-49 | 1189.773 | 1246.452 | 4.7639 | 5.740 | 24889 |
| 5 | 50-59 | 1189.773 | 1214.352 | 2.0658 | 5.515 | 15662 |
| 6 | 60-69 | 1189.773 | 1206.526 | 1.4080 | 5.469 | 21922 |
| 7 | 70-79 | 1189.773 | 1211.732 | 1.8456 | 5.603 | 16592 |
| 8 | 80-89 | 1189.773 | 1205.709 | 1.3394 | 4.815 | 23027 |
| 9 | 90-99 | 1189.773 | 1212.362 | 1.8986 | 4.657 | 23217 |

- Annual harvest minimum: 118,875,625.6 m3/yr.
- Annual harvest maximum: 124,645,243.0 m3/yr.
- Annual mean: 120,572,612.5 m3/yr.
- Annual CV: 0.013894.
- Annual floor met: `False`; gap to the nominal
  annual rate: 101,713.5 m3.
- Period shortfall: 0.0 m3.
- Sustained: `True`.
- Selected blocks: 204,771
  (55.071 Mha).
- Blocks reharvested within 100 years: 0.

## 3. Harvest by province

| Province | Control share | Target Mm3/yr | First period Mm3/yr | 100-year Mm3/yr | Area Mha | Blocks |
|---|---|---|---|---|---|---|
| BC | 33.602% | 39.978577 | 46.745194 | 42.011751 | 8.837 | 57958 |
| AB | 19.240% | 22.891404 | 23.326795 | 23.361289 | 7.494 | 27702 |
| SK | 3.652% | 4.344698 | 4.724230 | 4.542191 | 3.001 | 7412 |
| MB | 0.954% | 1.135236 | 1.186532 | 1.252543 | 0.874 | 1434 |
| ON | 11.341% | 13.493596 | 14.429683 | 13.905724 | 9.652 | 18185 |
| QC | 22.420% | 26.674334 | 27.002691 | 27.133219 | 20.943 | 74412 |
| NB | 5.240% | 6.234700 | 0.009632 | 4.446232 | 1.770 | 8801 |
| NS | 2.007% | 2.388245 | 0.000000 | 2.159822 | 1.000 | 2199 |
| PE | 0.254% | 0.302210 | 0.000000 | 0.172589 | 0.095 | 670 |
| NL | 1.222% | 1.454038 | 1.479877 | 1.499397 | 1.341 | 5447 |
| YT | 0.037% | 0.043926 | 0.044773 | 0.045284 | 0.026 | 209 |
| NT | 0.031% | 0.036376 | 0.037259 | 0.042572 | 0.039 | 342 |
| NU | 0.000% | 0.000000 | 0.000000 | 0.000000 | 0.000 | 0 |

## 4. Chain versus frozen v5.1

| Metric | Unit | v5.1 | First-period basis | Delta % | Achieved basis | Delta % |
|---|---|---|---|---|---|---|
| harvest_m3 | m3 | 118977339.100000 | 118986665.616576 | 0.0078 | 120572612.537194 | 1.3408 |
| solid_product_m3 | m3 | 37673626.761068 | 38721719.240067 | 2.7820 | 38331489.303681 | 1.7462 |
| sawlog_product_m3 | m3 | 33956989.460016 | 34901683.887452 | 2.7820 | 34549951.522504 | 1.7462 |
| panel_product_m3 | m3 | 3716637.301052 | 3820035.352615 | 2.7820 | 3781537.781177 | 1.7462 |
| pulp_product_odt | odt | 12066311.269557 | 11705393.633388 | -2.9911 | 12168143.591512 | 0.8439 |
| pellet_product_odt | odt | 5229686.166845 | 5294029.708367 | 1.2304 | 5349279.894404 | 2.2868 |
| bio_product_mwh | MWh | 930946.020335 | 942399.932100 | 1.2304 | 952235.118988 | 2.2868 |
| process_residue_m3 | m3 | 59910020.050504 | 60000019.232025 | 0.1502 | 60723224.946009 | 1.3574 |
| process_residue_odt | odt | 26959509.022727 | 27000008.654425 | 0.1502 | 27325451.225718 | 1.3574 |
| process_residue_pj | PJ | 498.750917 | 499.500160 | 0.1502 | 505.520848 | 1.3574 |
| harvest_residue_gross_odt | odt | 24022203.571695 | 23763877.022244 | -1.0754 | 24338134.607958 | 1.3152 |
| harvest_residue_gross_pj | PJ | 444.410766 | 439.631725 | -1.0754 | 450.255490 | 1.3152 |
| harvest_residue_recoverable_r035_odt | odt | 8407771.250093 | 8317356.957794 | -1.0754 | 8518347.112794 | 1.3152 |
| harvest_residue_recoverable_r035_pj | PJ | 155.543768 | 153.871104 | -1.0754 | 157.589422 | 1.3152 |
| harvest_residue_recoverable_r060_odt | odt | 14413322.143017 | 14258326.213359 | -1.0754 | 14602880.764786 | 1.3152 |
| harvest_residue_recoverable_r060_pj | PJ | 266.646460 | 263.779035 | -1.0754 | 270.153294 | 1.3152 |
| harvest_residue_recoverable_r075_odt | odt | 18016652.678771 | 17822907.766708 | -1.0754 | 18253600.955992 | 1.3152 |
| harvest_residue_recoverable_r075_pj | PJ | 333.308075 | 329.723794 | -1.0754 | 337.691618 | 1.3152 |
| total_residue_gross_pj | PJ | 943.161683 | 939.131885 | -0.4273 | 955.776338 | 1.3375 |
| total_residue_recoverable_r035_pj | PJ | 654.294685 | 653.371264 | -0.1411 | 663.110269 | 1.3473 |
| total_residue_recoverable_r060_pj | PJ | 765.397377 | 763.279195 | -0.2767 | 775.674142 | 1.3427 |
| total_residue_recoverable_r075_pj | PJ | 832.058991 | 829.223954 | -0.3407 | 843.212465 | 1.3405 |

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
- Provincial period targets use the frozen 119m allocated_share values. A final whole block may overshoot a provincial target because no block is split or scaled.
- Rotation is the integer age of maximum MAI on the RSYC yield curve, capped to 40-200 years; the raw peak is flagged.
- Frozen chain v5.1 coefficients are applied to WS4 harvest by origin province. Facility assignment, mill capacity, transport, and interprovincial trade are not re-run.
- The primary chain basis uses the first-period annual average; the secondary basis uses the 100-year achieved average. Neither is an official OSeCAN change.
