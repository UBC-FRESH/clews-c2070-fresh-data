# Sustainable 100 and 150 Mm3/yr WS4 Schedules and Chains

**Artifact:** `ws4_sustainable_cases` **Version:** 1.0.0

**Status:** pass. Both documented provincial ceiling cases are
simulated for 100 years on the national 990 m WS4 estate with the same
whole-block scheduler as the sustainable 119 Mm3 case. This is a model
estimate, not an AAC, policy result, tenure plan, or national supply claim.

**Labels:** `model_estimate=true`, `observed=false`, `policy_grade=false`,
`national_claim=false`, `ws4_derived=true`, `sustainable_schedule=true`,
`official_osecan_changed=false`, `chain_v51_unchanged=true`.

## 1. Schedule results

| Case | Target Mm3/yr | Annual min Mm3/yr | Annual max Mm3/yr | Annual mean Mm3/yr | Annual floor | Period shortfall Mm3 | Sustained | Blocks | Area Mha | Reharvested |
|---|---|---|---|---|---|---|---|---|---|---|
| 100m | 100.000000 | 100.0968 | 102.9553 | 101.1050 | True | 0.000000 | True | 267,389 | 71.659 | 0 |
| 150m | 150.000000 | 149.9970 | 153.4957 | 151.2477 | False | 0.000000 | True | 400,049 | 106.577 | 586 |

The control unit is the 10-year period. Both cases meet every period target
with zero period shortfall. The 150m case has one annual offset 149,997,027.4 m3, 2,972.8 m3 (0.0020%) below the nominal annual rate, while its minimum period is 1,501,156,257.2 m3, 1,156,255.2 m3 above the period target; this is a longest-processing-time spread residual and is reported, not forced.

## 2. Chain comparison against frozen v5.1

| Case | Metric | Unit | v5.1 | Primary | Delta % | Achieved | Delta % |
|---|---|---|---|---|---|---|---|
| 100m | harvest_m3 | m3 | 100,000,000.100000 | 100,176,736.535813 | 0.1767 | 101,104,998.307399 | 1.1050 |
| 100m | solid_product_m3 | m3 | 31,692,807.151334 | 31,734,986.724901 | 0.1331 | 31,936,905.274774 | 0.7702 |
| 100m | pulp_product_odt | odt | 10,136,702.863917 | 10,157,930.478736 | 0.2094 | 10,281,853.783595 | 1.4319 |
| 100m | process_residue_pj | PJ | 419.238018 | 419.956046 | 0.1713 | 423.797409 | 1.0875 |
| 100m | harvest_residue_gross_pj | PJ | 373.243923 | 374.055208 | 0.2174 | 378.082981 | 1.2965 |
| 100m | harvest_residue_recoverable_r060_pj | PJ | 223.946354 | 224.433125 | 0.2174 | 226.849788 | 1.2965 |
| 100m | total_residue_gross_pj | PJ | 792.481942 | 794.011254 | 0.1930 | 801.880390 | 1.1860 |
| 150m | harvest_m3 | m3 | 150,000,000.200000 | 153,371,076.210678 | 2.2474 | 151,247,672.316712 | 0.8318 |
| 150m | solid_product_m3 | m3 | 46,136,665.718213 | 46,741,639.058194 | 1.3113 | 46,414,539.794365 | 0.6023 |
| 150m | pulp_product_odt | odt | 15,550,881.011045 | 16,047,204.683579 | 3.1916 | 15,715,281.869293 | 1.0572 |
| 150m | process_residue_pj | PJ | 626.865219 | 640.905817 | 2.2398 | 632.046174 | 0.8265 |
| 150m | harvest_residue_gross_pj | PJ | 573.125413 | 590.557241 | 3.0415 | 578.744364 | 0.9804 |
| 150m | harvest_residue_recoverable_r060_pj | PJ | 343.875248 | 354.334345 | 3.0415 | 347.246619 | 0.9804 |
| 150m | total_residue_gross_pj | PJ | 1,199.990632 | 1,231.463058 | 2.6227 | 1,210.790538 | 0.9000 |

The primary basis applies frozen v5.1 per-province coefficients to the
first-period annual average; the achieved basis applies them to the 100-year
achieved annual average. Reference values are the frozen 100/150 Mm3 targets
in `data/derived/national/facilities/national_facility_chain_scenarios_v9/scenario_summary.csv`.

## 3. OSeCAN handoff

Rebuilt from the sustainable 100/150 WS4 case chains on the origin-province basis using the frozen handoff-v10 zone weights. Frozen v5.1 21/21 positions match handoff v10; 100 Mm3 primary/achieved 7/7, 7/7; 150 Mm3 7/7, 7/7. Official OSeCAN is unchanged.

## 4. Caveats

- The full forest estate is used; no operability, tenure, road, slope, or
  mill-capacity screen is applied.
- Whole blocks are selected; provincial overshoot is retained and reported.
- Rotation is capped to 40-200 years and never relaxed to meet a target.
- Frozen chain v5.1 and the official OSeCAN tree are read-only; no UI surface
  is changed.
