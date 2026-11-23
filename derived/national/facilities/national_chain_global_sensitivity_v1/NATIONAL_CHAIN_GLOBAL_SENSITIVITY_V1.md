# National Facility Chain Global Sensitivity V1

Global screening of the national facility chain at the 119 Mm3 provincial allocation. All values are model estimates: `model_estimate=true`, `observed=false`, `policy_grade=false`, `national_claim=false`. No policy, AAC, investment, or national-supply claim is made. No UI or official OSeCAN surface is changed.

## Design/factors

A 16-run Plackett-Burman/Hadamard array is used. The seven factor columns are a resolution-IV subset: every main effect is orthogonal to every other main effect and to every two-factor interaction among the seven factors. Two-factor interactions are aliased in triplets; they are not individually estimable without a foldover.

| Factor | PB low | PB high | Documented levels | Source |
|---|---|---|---|---|
| Capacity / assignment | local_v6 | trade_v5 | local_v6, trade_v5 | local v6 province_capacity_floor vs trade v5 published_plus_proxy |
| Product coefficients | donor_v1 | measured_v4 | donor_v1, measured_v4 | national_product_chain_v1 donor vs measured chain v4 |
| Residue basis | stem_only | stem_plus_branch_foliage | stem_only, stem_plus_branch_foliage | stem-only harvest residue vs measured stem + branch/foliage |
| Harvest recovery | 0.35 | 0.75 | 0.35, 0.6, 0.75 | documented 0.35/0.60/0.75 recovery scenarios; 0.60 is a reference value, not a calibrated factor |
| Process availability | 0.0 | 0.75 | 0.0, 0.25, 0.5, 0.75 | documented 0/25/50/75% process-availability screening cases |
| Price scenario | donor_flat | stumpage_scaled | donor_flat, stumpage_scaled | national_economics_v2_3 donor_flat base vs stumpage_scaled sensitivity |
| Zone weights | osecan_supply_dispatch | equal_split | osecan_supply_dispatch, equal_split | OSeCAN supply/dispatch weights vs equal split for multi-zone provinces; sub-provincial allocation only |

Factors 4 and 5 are multi-level in the source artifacts. The PB array screens their extreme levels (0.35 vs 0.75 recovery; 0 vs 75% availability). The intermediate 0.60 recovery and 25/50% availability cases are reported in the descriptive level sweep, not as PB main-effect contrasts.

### Design matrix

| Run | Assignment | Coefficients | Residue | Recovery | Availability | Price | Zone |
|---|---|---|---|---|---|---|---|
| PB01 | trade_v5 | measured_v4 | stem_plus_branch_foliage | 0.75 | 0.75 | stumpage_scaled | equal_split |
| PB02 | trade_v5 | measured_v4 | stem_plus_branch_foliage | 0.75 | 0 | donor_flat | osecan_supply_dispatch |
| PB03 | trade_v5 | measured_v4 | stem_only | 0.35 | 0.75 | stumpage_scaled | osecan_supply_dispatch |
| PB04 | trade_v5 | measured_v4 | stem_only | 0.35 | 0 | donor_flat | equal_split |
| PB05 | trade_v5 | donor_v1 | stem_plus_branch_foliage | 0.35 | 0.75 | donor_flat | equal_split |
| PB06 | trade_v5 | donor_v1 | stem_plus_branch_foliage | 0.35 | 0 | stumpage_scaled | osecan_supply_dispatch |
| PB07 | trade_v5 | donor_v1 | stem_only | 0.75 | 0.75 | donor_flat | osecan_supply_dispatch |
| PB08 | trade_v5 | donor_v1 | stem_only | 0.75 | 0 | stumpage_scaled | equal_split |
| PB09 | local_v6 | measured_v4 | stem_plus_branch_foliage | 0.35 | 0 | stumpage_scaled | equal_split |
| PB10 | local_v6 | measured_v4 | stem_plus_branch_foliage | 0.35 | 0.75 | donor_flat | osecan_supply_dispatch |
| PB11 | local_v6 | measured_v4 | stem_only | 0.75 | 0 | stumpage_scaled | osecan_supply_dispatch |
| PB12 | local_v6 | measured_v4 | stem_only | 0.75 | 0.75 | donor_flat | equal_split |
| PB13 | local_v6 | donor_v1 | stem_plus_branch_foliage | 0.75 | 0 | donor_flat | equal_split |
| PB14 | local_v6 | donor_v1 | stem_plus_branch_foliage | 0.75 | 0.75 | stumpage_scaled | osecan_supply_dispatch |
| PB15 | local_v6 | donor_v1 | stem_only | 0.35 | 0 | donor_flat | osecan_supply_dispatch |
| PB16 | local_v6 | donor_v1 | stem_only | 0.35 | 0.75 | stumpage_scaled | equal_split |

### Aliasing

| Alias group | Members | Aliased with |
|---|---|---|
| A1 | assignment*coefficients = residue*recovery = availability*price | dummy_column_3 |
| A2 | assignment*residue = coefficients*recovery = availability*zone | dummy_column_5 |
| A3 | assignment*recovery = coefficients*residue = price*zone | dummy_column_6 |
| A4 | assignment*availability = coefficients*price = residue*zone | dummy_column_8 |
| A5 | assignment*price = coefficients*availability = recovery*zone | dummy_column_11 |
| A6 | assignment*zone = residue*availability = recovery*price | dummy_column_13 |
| A7 | coefficients*zone = residue*price = recovery*availability | dummy_column_14 |

## Main effects ranking

Main effect = mean response at the PB high level minus mean response at the PB low level. Normalized effect = |effect| / largest |effect| for that response. The overall score is the mean normalized effect across the six required responses; it is a screening rank, not a variance decomposition. Effects below 0.0001 of the largest |effect| for a response are reported but treated as numerically negligible.

### Effect matrix

| Factor | National process residue | Harvest gross residue | Harvest recoverable residue | Total gross residue | National modeled margin | BC process residue |
|---|---|---|---|---|---|---|
| Capacity / assignment | +0.000 | +0.000 | +0.000 | +0.000 | +0.000 | +28.006 |
| Product coefficients | -4.272 | -39.918 | -21.955 | -44.190 | +0.000 | -0.917 |
| Residue basis | +0.000 | +185.780 | +102.179 | +185.780 | +0.000 | +0.000 |
| Harvest recovery | +0.000 | +0.000 | +96.284 | +0.000 | +0.000 | +0.000 |
| Process availability | +390.232 | +0.000 | +0.000 | +390.232 | +0.000 | +164.127 |
| Price scenario | +0.000 | +0.000 | +0.000 | +0.000 | -5,860.648 | +0.002 |
| Zone weights | +0.000 | +0.000 | +0.000 | +0.000 | +0.000 | +0.000 |

### Per-response top factors

| Response | Unit | Top three factors (effect) |
|---|---|---|
| National process residue | PJ | availability (+390.232); coefficients (-4.272); assignment (+0.000) |
| Harvest gross residue | PJ | residue (+185.780); coefficients (-39.918); assignment (+0.000) |
| Harvest recoverable residue | PJ | residue (+102.179); recovery (+96.284); coefficients (-21.955) |
| Total gross residue | PJ | availability (+390.232); residue (+185.780); coefficients (-44.190) |
| National modeled margin | M CAD | price (-5,860.648); assignment (+0.000); coefficients (+0.000) |
| BC process residue | PJ | availability (+164.127); assignment (+28.006); coefficients (-0.917) |

### Overall ranking

| Rank | Factor | Mean normalized |effect| | Material responses | Largest response |
|---|---|---|---|---|
| 1 | Process availability | 0.5000 | 3 | National process residue |
| 2 | Residue basis | 0.4127 | 3 | Harvest gross residue |
| 3 | Price scenario | 0.1667 | 1 | National modeled margin |
| 4 | Harvest recovery | 0.1571 | 1 | Harvest recoverable residue |
| 5 | Product coefficients | 0.0933 | 5 | Total gross residue |
| 6 | Capacity / assignment | 0.0284 | 1 | BC process residue |
| 7 | Zone weights | 0.0000 | 0 | none |

## Which factors matter

- **National process residue**: `availability` is the dominant screen (effect +390.232 PJ for the 0 vs 75% availability contrast). Assignment and residue basis do not change the national process total; the trade case moves the same process residue across provinces.
- **Harvest gross residue**: `residue` is the dominant screen (effect +185.780 PJ), followed by product coefficients. Assignment, recovery, availability, price and zone weights do not change gross harvest residue.
- **Harvest recoverable residue**: `residue` and `recovery` are the leading screens; recoverable residue is gross residue times recovery, so the two factors combine multiplicatively.
- **Total gross residue**: `availability` leads (effect +390.232 PJ), followed by residue basis and product coefficients. Total gross is the availability-adjusted process stream plus harvest gross, so it inherits both.
- **National modeled margin**: `price` is the only material screen (effect -5,860.648 M CAD). The margin file is a 119 Mm3 national economics diagnostic; the physical chain factors do not re-price it in the current model.
- **BC process residue**: `availability` leads (effect +164.127 PJ), with assignment second. Trade-v5 concentrates more process residue in BC than local-v6; national process totals are unchanged.
- **Zone weights**: the requested provincial/national responses are invariant by construction. The auxiliary `bc_b2_process_pj` diagnostic changes because the B2 weight moves from the OSeCAN supply share to an equal split; this is a sub-provincial dispatch effect, not a provincial total effect.

## Level sweep

One-at-a-time descriptive sweep from the baseline configuration (`local_v6`, `measured_v4`, stem + branch/foliage, 0.60 recovery, 50% availability, `donor_flat`, OSeCAN weights). It is not part of the PB array and does not estimate curvature.

| Varied factor | Level | Process PJ | Harvest gross PJ | Harvest recoverable PJ | Total gross PJ | BC process PJ |
|---|---|---|---|---|---|---|
| Capacity / assignment | local_v6 | 257.307 | 313.640 | 188.184 | 570.947 | 90.135 |
| Capacity / assignment | trade_v5 | 257.307 | 313.640 | 188.184 | 570.947 | 127.479 |
| Product coefficients | donor_v1 | 263.003 | 353.559 | 212.135 | 616.561 | 91.360 |
| Product coefficients | measured_v4 | 257.307 | 313.640 | 188.184 | 570.947 | 90.135 |
| Residue basis | stem_only | 257.307 | 127.860 | 76.716 | 385.167 | 90.135 |
| Residue basis | stem_plus_branch_foliage | 257.307 | 313.640 | 188.184 | 570.947 | 90.135 |
| Harvest recovery | 0.35 | 257.307 | 313.640 | 109.774 | 570.947 | 90.135 |
| Harvest recovery | 0.6 | 257.307 | 313.640 | 188.184 | 570.947 | 90.135 |
| Harvest recovery | 0.75 | 257.307 | 313.640 | 235.230 | 570.947 | 90.135 |
| Process availability | 0.0 | 0.000 | 313.640 | 188.184 | 313.640 | 0.000 |
| Process availability | 0.25 | 128.654 | 313.640 | 188.184 | 442.294 | 45.068 |
| Process availability | 0.5 | 257.307 | 313.640 | 188.184 | 570.947 | 90.135 |
| Process availability | 0.75 | 385.961 | 313.640 | 188.184 | 699.601 | 135.203 |
| Price scenario | donor_flat | 257.307 | 313.640 | 188.184 | 570.947 | 90.135 |
| Price scenario | stumpage_scaled | 257.307 | 313.640 | 188.184 | 570.947 | 90.135 |
| Zone weights | osecan_supply_dispatch | 257.307 | 313.640 | 188.184 | 570.947 | 90.135 |
| Zone weights | equal_split | 257.307 | 313.640 | 188.184 | 570.947 | 90.135 |

## Caveats

- Screening artifact at the 119 Mm3 provincial allocation; the 100 and 150 Mm3 cases are not screened here.
- PB is a two-level screening design. The 0.60 recovery and 25/50% process-availability levels are descriptive sweep points, not PB contrasts.
- Main effects are clear of two-factor interactions among the seven factors, but 2FIs are aliased in triplets and higher-order interactions are not resolved. No foldover was run.
- The donor + total-basis combination is a partial lower bound: donor provinces have no branch/foliage coefficient, so the measured branch/foliage increment is added only where a measured coefficient exists. It is flagged `residue_basis_complete=false`.
- The chain summary `harvest_residue_recoverable_pj` is the product-chain residue-feedstock quantity, not the 0.35/0.60/0.75 recovery scenario. This artifact defines recoverable as gross harvest residue x recovery, following the residue-curve documentation.
- Process residue is facility-assigned and harvest residue is origin-province only. Total gross is the availability-adjusted process stream plus harvest gross; it is not a combined OSeCAN row.
- National margin is the existing 119 Mm3 national-economics diagnostic. Physical chain factors do not re-price it in this screening artifact; only the price scenario changes the margin response.
- A tiny price-scenario effect can appear on BC process residue (about 0.002 PJ) through higher-order aliasing in the 16-run design; it is below the material-effect threshold and is not a physical price effect.
- Zone weights change sub-provincial dispatch only. Requested provincial and national responses are invariant by construction; the BC B2 diagnostic is auxiliary.
- Assignment local-v6 vs trade-v5 changes the facility distribution, not national products or process residue; BC process residue changes because facility location changes.
- Product coefficients donor-v1 vs measured-v4 replace only the four measured provinces (BC, QC, NB, YT); the other nine keep donor coefficients.
- All values are model estimates; observed=false and policy_grade=false. No policy, AAC, tenure, investment, interprovincial-trade, or national-supply claim is made.
- No UI or official OSeCAN surface is changed. OSeCAN zone weights are read only.

Labels: `model_estimate`, `observed=false`, `policy_grade=false`, `national_claim=false`.

## Tests/commits/status

Validation checks are listed in `summary.json` and the manifest. Run `.venv/bin/python -m pytest tests/test_national_chain_global_sensitivity.py` for the contract tests. No commit is created by the artifact builder; the orchestrator owns git operations.

Reproduce: `.venv/bin/python -m workflows.national.facilities.national_chain_global_sensitivity`
