# Sustainable 100 Mm3/yr WS4 Schedule and Chain

**Artifact:** `ws4_sustainable_100m` **Version:** 1.0.0

**Status:** pass. The 100,000,000.1 m3/yr case is sustained for 100 years. This is a whole-block model estimate, not an AAC, policy result, tenure plan, or investment case.

**Labels:** `model_estimate=true`, `observed=false`, `policy_grade=false`,
`national_claim=false`, `ws4_derived=true`, `sustainable_schedule=true`,
`official_osecan_changed=false`, `chain_v51_unchanged=true`.

## 1. Input and method

- Dataset: `data/derived/ws4/scanfi-national-990m/dataset`
- Schedule: `data/derived/ws4/sustainable-100m/schedule.csv`
- Run: `data/derived/ws4/sustainable-100m/run_100y`
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
| 0 | 0-9 | 1000.000 | 1001.767 | 0.1767 | 8.279 | 41111 |
| 1 | 10-19 | 1000.000 | 1026.566 | 2.6566 | 7.094 | 24273 |
| 2 | 20-29 | 1000.000 | 1015.860 | 1.5860 | 6.983 | 15037 |
| 3 | 30-39 | 1000.000 | 1001.491 | 0.1491 | 7.013 | 27758 |
| 4 | 40-49 | 1000.000 | 1007.269 | 0.7269 | 7.197 | 24823 |
| 5 | 50-59 | 1000.000 | 1012.530 | 1.2530 | 7.336 | 28528 |
| 6 | 60-69 | 1000.000 | 1014.236 | 1.4236 | 7.268 | 25995 |
| 7 | 70-79 | 1000.000 | 1005.275 | 0.5275 | 6.677 | 32375 |
| 8 | 80-89 | 1000.000 | 1017.304 | 1.7304 | 6.718 | 26337 |
| 9 | 90-99 | 1000.000 | 1008.201 | 0.8201 | 7.095 | 21152 |

- Annual harvest minimum: 100,096,807.1 m3/yr.
- Annual harvest maximum: 102,955,282.3 m3/yr.
- Annual mean: 101,104,998.3 m3/yr.
- Annual CV: 0.007418.
- Annual floor met: `True`; gap to the nominal
  annual rate: 0.0 m3.
- Period shortfall: 0.0 m3.
- Sustained: `True`.
- Selected blocks: 267,389
  (71.659 Mha).
- Blocks reharvested within 100 years: 0.

## 3. Harvest by province

| Province | Control share | Target Mm3/yr | First period Mm3/yr | 100-year Mm3/yr | Area Mha | Blocks |
|---|---|---|---|---|---|---|
| BC | 33.249% | 33.248823 | 33.251301 | 33.254767 | 13.363 | 92512 |
| AB | 19.038% | 19.038002 | 19.106716 | 19.276570 | 9.762 | 29832 |
| SK | 3.613% | 3.613337 | 3.635680 | 3.644138 | 3.404 | 8765 |
| MB | 0.944% | 0.944137 | 0.944855 | 1.062180 | 1.171 | 2583 |
| ON | 11.222% | 11.222165 | 11.232355 | 11.410957 | 11.403 | 24217 |
| QC | 22.184% | 22.184137 | 22.193582 | 22.336965 | 25.406 | 80845 |
| NB | 6.235% | 6.234700 | 6.269229 | 6.251985 | 3.498 | 15941 |
| NS | 1.986% | 1.986222 | 2.003244 | 2.328170 | 1.571 | 3479 |
| PE | 0.251% | 0.251338 | 0.257298 | 0.258346 | 0.193 | 1294 |
| NL | 1.209% | 1.209274 | 1.209345 | 1.211042 | 1.804 | 7210 |
| YT | 0.037% | 0.036532 | 0.037280 | 0.037550 | 0.039 | 320 |
| NT | 0.031% | 0.031333 | 0.035851 | 0.032327 | 0.044 | 391 |
| NU | 0.000% | 0.000000 | 0.000000 | 0.000000 | 0.000 | 0 |

## 4. Chain versus frozen v5.1

| Metric | Unit | v5.1 | First-period basis | Delta % | Achieved basis | Delta % |
|---|---|---|---|---|---|---|
| harvest_m3 | m3 | 100000000.100000 | 100176736.535813 | 0.1767 | 101104998.307399 | 1.1050 |
| solid_product_m3 | m3 | 31692807.151334 | 31734986.724901 | 0.1331 | 31936905.274774 | 0.7702 |
| sawlog_product_m3 | m3 | 28566198.981094 | 28604217.389679 | 0.1331 | 28786215.956297 | 0.7702 |
| panel_product_m3 | m3 | 3126608.170239 | 3130769.335222 | 0.1331 | 3150689.318477 | 0.7702 |
| pulp_product_odt | odt | 10136702.863917 | 10157930.478736 | 0.2094 | 10281853.783595 | 1.4319 |
| pellet_product_odt | odt | 4372287.851260 | 4384225.196376 | 0.2730 | 4438052.524042 | 1.5041 |
| bio_product_mwh | MWh | 778318.974606 | 780443.963291 | 0.2730 | 790025.864551 | 1.5041 |
| process_residue_m3 | m3 | 50358921.112605 | 50445170.697792 | 0.1713 | 50906595.696776 | 1.0875 |
| process_residue_odt | odt | 22661514.500672 | 22700326.814019 | 0.1713 | 22907968.063562 | 1.0875 |
| process_residue_pj | PJ | 419.238018 | 419.956046 | 0.1713 | 423.797409 | 1.0875 |
| harvest_residue_gross_odt | odt | 20175347.205464 | 20219200.429437 | 0.2174 | 20436917.879920 | 1.2965 |
| harvest_residue_gross_pj | PJ | 373.243923 | 374.055208 | 0.2174 | 378.082981 | 1.2965 |
| harvest_residue_recoverable_r035_odt | odt | 7061371.521912 | 7076720.150310 | 0.2174 | 7152921.257980 | 1.2965 |
| harvest_residue_recoverable_r035_pj | PJ | 130.635373 | 130.919323 | 0.2174 | 132.329043 | 1.2965 |
| harvest_residue_recoverable_r060_odt | odt | 12105208.323278 | 12131520.257670 | 0.2174 | 12262150.727961 | 1.2965 |
| harvest_residue_recoverable_r060_pj | PJ | 223.946354 | 224.433125 | 0.2174 | 226.849788 | 1.2965 |
| harvest_residue_recoverable_r075_odt | odt | 15131510.404098 | 15164400.322096 | 0.2174 | 15327688.409959 | 1.2965 |
| harvest_residue_recoverable_r075_pj | PJ | 279.932942 | 280.541406 | 0.2174 | 283.562236 | 1.2965 |
| total_residue_gross_pj | PJ | 792.481942 | 794.011254 | 0.1930 | 801.880390 | 1.1860 |
| total_residue_recoverable_r035_pj | PJ | 549.873391 | 550.875369 | 0.1822 | 556.126452 | 1.1372 |
| total_residue_recoverable_r060_pj | PJ | 643.184372 | 644.389171 | 0.1873 | 650.647198 | 1.1603 |
| total_residue_recoverable_r075_pj | PJ | 699.170961 | 700.497452 | 0.1897 | 707.359645 | 1.1712 |

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
