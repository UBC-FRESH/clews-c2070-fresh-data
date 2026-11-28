# Sustainable 100 Mm3/yr WS4 Schedule and Chain

**Artifact:** `ws4_transformed_sustainable_100m` **Version:** 1.0.0

**Status:** pass. The 100,000,000.1 m3/yr case is sustained for 100 years. This is a whole-block model estimate, not an AAC, policy result, tenure plan, or investment case.

**Labels:** `model_estimate=true`, `observed=false`, `policy_grade=false`,
`national_claim=false`, `ws4_derived=true`, `sustainable_schedule=true`,
`transformed_curves=true`, `official_osecan_changed=false`,
`chain_v51_unchanged=true`.

## 1. Input and method

- Dataset: `data/derived/ws4/scanfi-national-990m-transformed/dataset`
- Schedule: `data/derived/ws4/scanfi-national-990m-transformed/sustainable-100m/schedule.csv`
- Run: `data/derived/ws4/scanfi-national-990m-transformed/sustainable-100m/run_100y`
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
| 0 | 0-9 | 1000.000 | 1007.106 | 0.7106 | 7.415 | 36483 |
| 1 | 10-19 | 1000.000 | 1031.923 | 3.1923 | 6.322 | 21181 |
| 2 | 20-29 | 1000.000 | 1017.814 | 1.7814 | 6.187 | 11337 |
| 3 | 30-39 | 1000.000 | 1005.078 | 0.5078 | 6.168 | 21235 |
| 4 | 40-49 | 1000.000 | 1004.347 | 0.4347 | 6.298 | 20834 |
| 5 | 50-59 | 1000.000 | 1015.818 | 1.5818 | 6.346 | 21808 |
| 6 | 60-69 | 1000.000 | 1013.633 | 1.3633 | 6.078 | 16839 |
| 7 | 70-79 | 1000.000 | 1010.498 | 1.0498 | 5.624 | 23475 |
| 8 | 80-89 | 1000.000 | 1002.499 | 0.2499 | 5.624 | 22049 |
| 9 | 90-99 | 1000.000 | 1003.492 | 0.3492 | 5.671 | 17329 |

- Annual harvest minimum: 100,249,852.2 m3/yr.
- Annual harvest maximum: 103,192,267.5 m3/yr.
- Annual mean: 101,122,055.0 m3/yr.
- Annual CV: 0.008491.
- Annual floor met: `True`; gap to the nominal
  annual rate: 0.0 m3.
- Period shortfall: 0.0 m3.
- Sustained: `True`.
- Selected blocks: 212,570
  (61.733 Mha).
- Blocks reharvested within 100 years: 0.

## 3. Harvest by province

| Province | Control share | Target Mm3/yr | First period Mm3/yr | 100-year Mm3/yr | Area Mha | Blocks |
|---|---|---|---|---|---|---|
| BC | 33.249% | 33.248823 | 33.256738 | 33.254672 | 6.809 | 42589 |
| AB | 19.038% | 19.038002 | 19.344024 | 19.290487 | 6.966 | 27064 |
| SK | 3.613% | 3.613337 | 3.735268 | 3.730773 | 2.944 | 7353 |
| MB | 0.944% | 0.944137 | 0.993436 | 0.975458 | 0.945 | 1813 |
| ON | 11.222% | 11.222165 | 11.414464 | 11.357771 | 11.357 | 24161 |
| QC | 22.184% | 22.184137 | 22.197008 | 22.394661 | 25.562 | 81055 |
| NB | 6.235% | 6.234700 | 6.241909 | 6.245190 | 3.516 | 15958 |
| NS | 1.986% | 1.986222 | 1.995216 | 2.323636 | 1.576 | 3492 |
| PE | 0.251% | 0.251338 | 0.251498 | 0.258435 | 0.193 | 1294 |
| NL | 1.209% | 1.209274 | 1.209514 | 1.219165 | 1.813 | 7324 |
| YT | 0.037% | 0.036532 | 0.039808 | 0.038061 | 0.022 | 184 |
| NT | 0.031% | 0.031333 | 0.031728 | 0.033746 | 0.030 | 283 |
| NU | 0.000% | 0.000000 | 0.000000 | 0.000000 | 0.000 | 0 |

## 4. Chain versus frozen v5.1

| Metric | Unit | v5.1 | First-period basis | Delta % | Achieved basis | Delta % |
|---|---|---|---|---|---|---|
| harvest_m3 | m3 | 100000000.100000 | 100710612.145284 | 0.7106 | 101122055.001091 | 1.1221 |
| solid_product_m3 | m3 | 31692807.151334 | 31855830.870359 | 0.5144 | 31915916.256395 | 0.7040 |
| sawlog_product_m3 | m3 | 28566198.981094 | 28713139.830293 | 0.5144 | 28767297.579247 | 0.7040 |
| panel_product_m3 | m3 | 3126608.170239 | 3142691.040065 | 0.5144 | 3148618.677147 | 0.7040 |
| pulp_product_odt | odt | 10136702.863917 | 10220847.937901 | 0.8301 | 10286376.089621 | 1.4765 |
| pellet_product_odt | odt | 4372287.851260 | 4433485.709789 | 1.3997 | 4460535.557480 | 2.0183 |
| bio_product_mwh | MWh | 778318.974606 | 789212.917576 | 1.3997 | 794028.110544 | 2.0183 |
| process_residue_m3 | m3 | 50358921.112605 | 50701902.057043 | 0.6811 | 50906591.758047 | 1.0875 |
| process_residue_odt | odt | 22661514.500672 | 22815855.925682 | 0.6811 | 22907966.291134 | 1.0875 |
| process_residue_pj | PJ | 419.238018 | 422.093335 | 0.6811 | 423.797376 | 1.0875 |
| harvest_residue_gross_odt | odt | 20175347.205464 | 20360773.892279 | 0.9191 | 20478260.585842 | 1.5014 |
| harvest_residue_gross_pj | PJ | 373.243923 | 376.674317 | 0.9191 | 378.847821 | 1.5014 |
| harvest_residue_recoverable_r035_odt | odt | 7061371.521912 | 7126270.862305 | 0.9191 | 7167391.205052 | 1.5014 |
| harvest_residue_recoverable_r035_pj | PJ | 130.635373 | 131.836011 | 0.9191 | 132.596737 | 1.5014 |
| harvest_residue_recoverable_r060_odt | odt | 12105208.323278 | 12216464.335376 | 0.9191 | 12286956.351514 | 1.5014 |
| harvest_residue_recoverable_r060_pj | PJ | 223.946354 | 226.004590 | 0.9191 | 227.308693 | 1.5014 |
| harvest_residue_recoverable_r075_odt | odt | 15131510.404098 | 15270580.419228 | 0.9191 | 15358695.439400 | 1.5014 |
| harvest_residue_recoverable_r075_pj | PJ | 279.932942 | 282.505738 | 0.9191 | 284.135866 | 1.5014 |
| total_residue_gross_pj | PJ | 792.481942 | 798.767652 | 0.7932 | 802.645197 | 1.2825 |
| total_residue_recoverable_r035_pj | PJ | 549.873391 | 553.929346 | 0.7376 | 556.394114 | 1.1859 |
| total_residue_recoverable_r060_pj | PJ | 643.184372 | 648.097925 | 0.7639 | 651.106069 | 1.2316 |
| total_residue_recoverable_r075_pj | PJ | 699.170961 | 704.599072 | 0.7764 | 707.933242 | 1.2532 |

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
