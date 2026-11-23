# National Facility Chain Global Sensitivity V2 (E1+E2c)

Global screening of the v4 E1 + E2c national facility chain at the 119 Mm3 provincial allocation. All values are model estimates: `model_estimate=true`, `observed=false`, `policy_grade=false`, `national_claim=false`. No policy, AAC, investment, or national-supply claim is made. No UI or official OSeCAN surface is changed.

## v4 design/responses

A 16-run Plackett-Burman/Hadamard array is used. The seven factor columns are a resolution-IV subset: every main effect is orthogonal to every other main effect and to every two-factor interaction among the seven factors. Two-factor interactions are aliased in triplets; they are not individually estimable without a foldover.

| Factor | PB low | PB high | Documented levels | Source |
|---|---|---|---|---|
| Capacity / assignment | local_v6 | trade_v5 | local_v6, trade_v5 | local v6 province_capacity_floor vs trade v5 published_plus_proxy; both levels use the same E2c or donor coefficient source |
| Product coefficients | donor_v1 | e2c | donor_v1, e2c | donor product chain v1 vs E1 measured + E2c product chain v5 (nine density-calibrated provinces, four measured provinces) |
| Residue basis | stem_only | stem_plus_branch_foliage | stem_only, stem_plus_branch_foliage | stem-only harvest residue vs stem + branch/foliage; donor-total adds only the measured four-province branch/foliage increment |
| Harvest recovery | 0.35 | 0.75 | 0.35, 0.6, 0.75 | documented 0.35/0.60/0.75 recovery scenarios; 0.60 is a reference value, not a calibrated factor |
| Process availability | 0.0 | 0.75 | 0.0, 0.25, 0.5, 0.75 | documented 0/25/50/75% process-availability screening cases |
| Price scenario | donor_flat | stumpage_scaled | donor_flat, stumpage_scaled | national_economics_v2_3 donor_flat base vs stumpage_scaled sensitivity (same v2.3 margin totals as v1) |
| Zone weights | osecan_supply_dispatch | equal_split | osecan_supply_dispatch, equal_split | OSeCAN handoff v8 supply/dispatch weights vs equal split for multi-zone provinces; sub-provincial allocation only |

Factors 4 and 5 are multi-level in the source artifacts. The PB array screens their extreme levels (0.35 vs 0.75 recovery; 0 vs 75% availability). The intermediate 0.60 recovery and 25/50% availability cases are reported in the descriptive level sweep, not as PB main-effect contrasts.

### Design matrix

| Run | Assignment | Coefficients | Residue | Recovery | Availability | Price | Zone |
|---|---|---|---|---|---|---|---|
| PB01 | trade_v5 | e2c | stem_plus_branch_foliage | 0.75 | 0.75 | stumpage_scaled | equal_split |
| PB02 | trade_v5 | e2c | stem_plus_branch_foliage | 0.75 | 0 | donor_flat | osecan_supply_dispatch |
| PB03 | trade_v5 | e2c | stem_only | 0.35 | 0.75 | stumpage_scaled | osecan_supply_dispatch |
| PB04 | trade_v5 | e2c | stem_only | 0.35 | 0 | donor_flat | equal_split |
| PB05 | trade_v5 | donor_v1 | stem_plus_branch_foliage | 0.35 | 0.75 | donor_flat | equal_split |
| PB06 | trade_v5 | donor_v1 | stem_plus_branch_foliage | 0.35 | 0 | stumpage_scaled | osecan_supply_dispatch |
| PB07 | trade_v5 | donor_v1 | stem_only | 0.75 | 0.75 | donor_flat | osecan_supply_dispatch |
| PB08 | trade_v5 | donor_v1 | stem_only | 0.75 | 0 | stumpage_scaled | equal_split |
| PB09 | local_v6 | e2c | stem_plus_branch_foliage | 0.35 | 0 | stumpage_scaled | equal_split |
| PB10 | local_v6 | e2c | stem_plus_branch_foliage | 0.35 | 0.75 | donor_flat | osecan_supply_dispatch |
| PB11 | local_v6 | e2c | stem_only | 0.75 | 0 | stumpage_scaled | osecan_supply_dispatch |
| PB12 | local_v6 | e2c | stem_only | 0.75 | 0.75 | donor_flat | equal_split |
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
| Capacity / assignment | +0.000 | +0.000 | +13.080 | +0.000 | +0.000 | +27.466 |
| Product coefficients | -10.220 | +25.453 | +13.999 | +15.232 | +0.000 | -1.030 |
| Residue basis | +0.000 | +251.179 | +138.149 | +251.179 | +0.000 | +0.000 |
| Harvest recovery | +0.000 | +0.000 | +109.358 | +0.000 | +0.000 | +0.000 |
| Process availability | +384.284 | +0.000 | +0.000 | +384.284 | +0.000 | +164.014 |
| Price scenario | +0.000 | +0.000 | +0.000 | +0.000 | -5,860.648 | -0.539 |
| Zone weights | +0.000 | +0.000 | +0.000 | +0.000 | +0.000 | +0.000 |

### Per-response top factors

| Response | Unit | Top three factors (effect) |
|---|---|---|
| National process residue | PJ | availability (+384.284); coefficients (-10.220); assignment (+0.000) |
| Harvest gross residue | PJ | residue (+251.179); coefficients (+25.453); assignment (+0.000) |
| Harvest recoverable residue | PJ | residue (+138.149); recovery (+109.358); coefficients (+13.999) |
| Total gross residue | PJ | availability (+384.284); residue (+251.179); coefficients (+15.232) |
| National modeled margin | M CAD | price (-5,860.648); assignment (+0.000); coefficients (+0.000) |
| BC process residue | PJ | availability (+164.014); assignment (+27.466); coefficients (-1.030) |

### Overall ranking

| Rank | Factor | Mean normalized |effect| | Material responses | Largest response |
|---|---|---|---|---|
| 1 | Process availability | 0.5000 | 3 | National process residue |
| 2 | Residue basis | 0.4423 | 3 | Total gross residue |
| 3 | Price scenario | 0.1672 | 2 | National modeled margin |
| 4 | Harvest recovery | 0.1319 | 1 | Harvest recoverable residue |
| 5 | Product coefficients | 0.0459 | 5 | Harvest gross residue |
| 6 | Capacity / assignment | 0.0437 | 2 | BC process residue |
| 7 | Zone weights | 0.0000 | 0 | none |

## Ranking v1 vs v2

v1 was built on the pre-E2 chain: its `measured_v4` level was the E1 four-province measured chain v4, not E2 v1. This refresh replaces that level with E1 measured + E2c. Ranks below compare the committed v1 artifact with this v4 artifact.

| Factor | v1 rank | v2 rank | Rank change | v1 score | v2 score | Note |
|---|---|---|---|---|---|---|
| Process availability | 1 | 1 | +0 | 0.5000 | 0.5000 |  |
| Residue basis | 2 | 2 | +0 | 0.4127 | 0.4423 |  |
| Price scenario | 3 | 3 | +0 | 0.1667 | 0.1672 |  |
| Harvest recovery | 4 | 4 | +0 | 0.1571 | 0.1319 |  |
| Product coefficients | 5 | 5 | +0 | 0.0933 | 0.0459 | level definition changed: v1 measured_v4 was the E1 four-province chain v4; v2 e2c is E1 measured + E2c for 13 provinces |
| Capacity / assignment | 6 | 6 | +0 | 0.0284 | 0.0437 |  |
| Zone weights | 7 | 7 | +0 | 0.0000 | 0.0000 | same OSeCAN BC weights in handoff v6 and v8 |

The overall order is unchanged, but the scores move: product coefficients and harvest recovery fall, while residue basis and capacity/assignment rise. The coefficient-level definition changed from E1 four-province measured to E1 + E2c, so the coefficient score is not a like-for-like evidence comparison.

## Which factors matter

- **National process residue**: `availability` is the dominant screen (effect +384.284 PJ for the 0 vs 75% availability contrast). Assignment and residue basis do not change the national process total.
- **Harvest gross residue**: `residue` leads (effect +251.179 PJ), followed by product coefficients. Assignment, recovery, availability, price and zone weights do not change gross harvest residue.
- **Harvest recoverable residue**: `residue` and `recovery` are the leading screens; recoverable residue is gross residue times recovery. The capacity/assignment main effect (+13.080 PJ) is a three-factor aliasing artifact, not a physical assignment effect.
- **Total gross residue**: `availability` leads (effect +384.284 PJ), followed by residue basis and product coefficients. Total gross inherits the availability-adjusted process stream plus harvest gross.
- **National modeled margin**: `price` is the only material screen (effect -5,860.648 M CAD). The margin file is the economics v2.3 119 Mm3 diagnostic; physical chain factors do not re-price it.
- **BC process residue**: `availability` leads (effect +164.014 PJ), with `assignment` second. Trade-v5 concentrates more process residue in BC than local-v6; national process totals are unchanged. The small price-scenario BC effect (-0.539 PJ) is a three-factor aliasing artifact, not a physical price effect.
- **Zone weights**: requested provincial/national responses are invariant by construction. The auxiliary `bc_b2_process_pj` diagnostic changes because the B2 weight moves from the OSeCAN supply share to an equal split; this is a sub-provincial dispatch effect.

## Level sweep

One-at-a-time descriptive sweep from the baseline configuration (`local_v6`, `e2c`, stem + branch/foliage, 0.60 recovery, 50% availability, `donor_flat`, OSeCAN v8 weights). It is not part of the PB array and does not estimate curvature.

| Varied factor | Level | Process PJ | Harvest gross PJ | Harvest recoverable PJ | Total gross PJ | BC process PJ |
|---|---|---|---|---|---|---|
| Capacity / assignment | local_v6 | 249.375 | 444.411 | 266.646 | 693.786 | 90.705 |
| Capacity / assignment | trade_v5 | 249.375 | 444.411 | 266.646 | 693.786 | 126.607 |
| Product coefficients | donor_v1 | 263.003 | 353.559 | 212.135 | 616.561 | 91.360 |
| Product coefficients | e2c | 249.375 | 444.411 | 266.646 | 693.786 | 90.705 |
| Residue basis | stem_only | 249.375 | 127.832 | 76.699 | 377.207 | 90.705 |
| Residue basis | stem_plus_branch_foliage | 249.375 | 444.411 | 266.646 | 693.786 | 90.705 |
| Harvest recovery | 0.35 | 249.375 | 444.411 | 155.544 | 693.786 | 90.705 |
| Harvest recovery | 0.6 | 249.375 | 444.411 | 266.646 | 693.786 | 90.705 |
| Harvest recovery | 0.75 | 249.375 | 444.411 | 333.308 | 693.786 | 90.705 |
| Process availability | 0.0 | 0.000 | 444.411 | 266.646 | 444.411 | 0.000 |
| Process availability | 0.25 | 124.688 | 444.411 | 266.646 | 569.098 | 45.352 |
| Process availability | 0.5 | 249.375 | 444.411 | 266.646 | 693.786 | 90.705 |
| Process availability | 0.75 | 374.063 | 444.411 | 266.646 | 818.474 | 136.057 |
| Price scenario | donor_flat | 249.375 | 444.411 | 266.646 | 693.786 | 90.705 |
| Price scenario | stumpage_scaled | 249.375 | 444.411 | 266.646 | 693.786 | 90.705 |
| Zone weights | osecan_supply_dispatch | 249.375 | 444.411 | 266.646 | 693.786 | 90.705 |
| Zone weights | equal_split | 249.375 | 444.411 | 266.646 | 693.786 | 90.705 |

## What changed

- The coefficient level moved from v1 `measured_v4` (E1 four-province chain v4) to `e2c` (E1 measured + E2c product chain v5). Nine jurisdictions now use E2c density-calibrated product and total-residue coefficients; measured BC/QC/NB/YT are unchanged.
- The local chain moved from v4/v5 to chain v7 and facility residue supply v7. Process residue falls from 514.614 to 498.751 PJ and total harvest gross rises from 313.640 to 444.411 PJ at 119 Mm3, before availability and recovery.
- E2c branch/foliage is now available for all 13 provinces. The E2c-total level uses the full E2c branch/foliage component (316.579 PJ). The donor-total level remains a partial lower bound: it adds only the measured four-province branch/foliage increment (185.780 PJ).
- The trade E2c source is derived from facility residue supply v7_trade. National process and harvest totals are assignment-invariant; BC process residue moves from 181.409 to 253.214 PJ.
- Zone weights are read from OSeCAN handoff v8 instead of v6. The BC B1/B2 weights are unchanged, so the zone-weight screen remains zero for provincial/national responses.
- Economics v2.3 margin values are unchanged from v1 (`donor_flat` 5,205.329 M CAD; `stumpage_scaled` -655.319 M CAD).
- The v1 artifact used the E1 four-province measured level, not E2 v1. The task brief's 'E2 v1 baseline' label does not match the committed v1 inputs; this is recorded explicitly.

## Caveats

- Screening artifact at the 119 Mm3 provincial allocation; the 100 and 150 Mm3 cases are not screened here.
- PB is a two-level screening design. The 0.60 recovery and 25/50% process-availability levels are descriptive sweep points, not PB contrasts.
- Main effects are clear of two-factor interactions among the seven factors, but 2FIs are aliased in triplets and higher-order interactions are not resolved. No foldover was run.
- Three-factor interactions are aliased with main effects in this 16-run resolution-IV design. The price-scenario effect on BC process residue (-0.539 PJ) and the assignment effect on harvest recoverable residue (+13.080 PJ) are three-factor aliasing artifacts, not physical price or assignment effects.
- The donor + total-basis combination is a partial lower bound: donor provinces have no donor branch/foliage coefficient, so only the measured four-province branch/foliage increment is added. It is flagged `residue_basis_complete=false`.
- E2c-total includes E2c branch/foliage for all 13 provinces. The E2c-vs-donor coefficient effect at total basis therefore includes both the stem-residue coefficient change and the E2c branch/foliage coverage change.
- The v1 artifact used the E1 four-province chain v4 as its `measured_v4` level, not E2 v1. This refresh compares v4 E1+E2c against that committed v1 baseline.
- The trade E2c source is derived from facility residue supply v7_trade. National process and harvest totals are assignment-invariant by construction; only the facility-province distribution, including BC process residue, changes.
- Process residue is facility-assigned and harvest residue is origin-province only. Total gross is the availability-adjusted process stream plus harvest gross; it is not a combined OSeCAN row.
- National margin is the existing economics v2.3 119 Mm3 diagnostic. Physical chain factors do not re-price it; only the price scenario changes the margin response.
- A price-scenario effect can appear on BC process residue through higher-order aliasing in the 16-run design; it is not a physical price effect.
- Zone weights change sub-provincial dispatch only. Requested provincial and national responses are invariant by construction; the BC B2 diagnostic is auxiliary.
- Assignment local-v6 vs trade-v5 changes the facility distribution, not national products or process residue; BC process residue changes because facility location changes. The trade case is a screening counterfactual, not an interprovincial trade forecast.
- Product coefficients donor-v1 vs E2c replace all 13 jurisdictions' product and residue coefficients; BC/QC/NB/YT remain measured, the other nine are E2c density-calibrated open-data estimates.
- All values are model estimates; observed=false and policy_grade=false. No policy, AAC, tenure, investment, interprovincial-trade, or national-supply claim is made.
- No UI or official OSeCAN surface is changed. OSeCAN handoff v8 zone weights are read only.

Labels: `model_estimate`, `observed=false`, `policy_grade=false`, `national_claim=false`, `screening_only=true`.

## Tests/commits/tag/status

Validation checks are listed in `summary.json` and the manifest. Run `.venv/bin/python -m pytest tests/test_national_chain_global_sensitivity_v2.py` for the contract tests. The artifact builder does not create a commit; the orchestrator owns git operations.

Reproduce: `.venv/bin/python -m workflows.national.facilities.national_chain_global_sensitivity_v2`
