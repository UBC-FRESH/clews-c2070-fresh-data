# Transport-Aware National Facility Assignment V9

Status: **model estimate screening** — `evidence_label=model_estimate`, `observed=false`, `policy_grade=false`. No national claim and no official OSeCAN change.

## 1. Transport cost v8

Transport cost is the committed transport cost v1 truck model (52.5 m3 base payload, empty return, 2026 CAD). Row cost = assigned m3 x cost/m3 at the row road distance. Energy is held at the base 4.07 GJ/m3 (0.22 ODT/m3 x 18.5 GJ/ODT) so low/high columns express cost-parameter uncertainty only.

- Assigned: **118,977,339 m3/yr**; transport cost: **6.817 billion CAD/yr**; **57.30 CAD/m3**; **14.078 CAD/GJ**.
- Assigned-volume-weighted mean road distance: **558.5 km**; maximum row distance: **1,527.0 km**.
- Facility count with positive assignment: **208**; proxy share of assigned volume: **0.3989**.

### Tier face-value comparison (v8 primary)

| Tier | Tier CAD/GJ | Volume above | Share above | Facilities above | Delivered CAD/GJ |
|---|---|---|---|---|---|
| T1 | 2.457 | 112,240,750 | 0.9434 | 188 | 16.535 |
| T2 | 2.457 | 112,240,750 | 0.9434 | 188 | 16.535 |
| T3 | 3.194 | 109,950,490 | 0.9241 | 183 | 17.272 |
| T4 | 3.500 | 109,950,490 | 0.9241 | 183 | 17.578 |

> Face-value comparison only: the supply-curve field is named variable_cost_usd_per_gj, but no currency or price-year conversion is documented; transport is 2026 CAD/GJ. Tier costs are adopted scenario values, not fitted marginal costs. T4 is a documented scenario high-cost tier. This is a screening arithmetic comparison, not a policy claim.

## 2. V9 assignment

V9 is a bipartite transportation linear program. It minimises modelled transport cost plus a local-preference penalty, subject to every provincial offer equality and every finite facility capacity. The penalty is the v8 documented 500 km cross-border rule expressed in 2026 CAD/m3 through the same transport curve (**51.45 CAD/m3**). Capacity v3 and the 1.2x provincial floor are unchanged. Products and residue are not recalculated or written.

- Assigned: **118,977,339 m3/yr**; transport cost: **6.382 billion CAD/yr**; **53.64 CAD/m3**; **13.180 CAD/GJ**.
- Mean road distance **522.0 km**; maximum row distance **1,462.5 km**; facilities used **203**.
- Local volume **118,940,963 m3/yr**; cross-border **36,376 m3/yr** (0.000306 share); proxy share **0.5287**.

### V9 province summary

| Province | Offer | Local | Cross | Mean km | Cost CAD | CAD/GJ | Facilities |
|---|---|---|---|---|---|---|---|
| AB | 22,891,404 | 22,891,404 | 0 | 228.5 | 557,224,009 | 5.981 | 15 |
| BC | 39,978,577 | 39,978,577 | 0 | 220.2 | 939,786,060 | 5.776 | 49 |
| MB | 1,135,236 | 1,135,236 | 0 | 787.6 | 91,011,928 | 19.698 | 4 |
| NB | 6,234,700 | 6,234,700 | 0 | 159.0 | 108,452,345 | 4.274 | 22 |
| NL | 1,454,038 | 1,454,038 | 0 | 947.7 | 139,824,901 | 23.627 | 1 |
| NS | 2,388,245 | 2,388,245 | 0 | 56.6 | 17,126,518 | 1.762 | 8 |
| NT | 36,376 | 0 | 36,376 | 1,147.0 | 4,221,979 | 28.517 | 1 |
| ON | 13,493,596 | 13,493,596 | 0 | 700.8 | 964,776,640 | 17.567 | 30 |
| PE | 302,210 | 302,210 | 0 | 66.1 | 2,453,763 | 1.995 | 2 |
| QC | 26,674,334 | 26,674,334 | 0 | 1,267.7 | 3,417,452,910 | 31.479 | 67 |
| SK | 4,344,698 | 4,344,698 | 0 | 302.1 | 137,678,937 | 7.786 | 3 |
| YT | 43,926 | 43,926 | 0 | 549.7 | 2,477,955 | 13.861 | 1 |

## 3. V8 versus V9

| Metric | Unit | V8 | V9 | Delta | Delta % |
|---|---|---|---|---|---|
| assigned_m3 | m3/yr | 118,977,339.1000 | 118,977,339.1000 | 0.0000 | 0.00 |
| local_m3 | m3/yr | 118,940,963.1000 | 118,940,963.1000 | 0.0000 | 0.00 |
| local_share | share | 0.9997 | 0.9997 | 0.0000 | 0.00 |
| cross_border_m3 | m3/yr | 36,376.0000 | 36,376.0000 | 0.0000 | 0.00 |
| cross_border_share | share | 0.0003 | 0.0003 | -0.0000 | -0.00 |
| published_m3 | m3/yr | 71,513,883.3077 | 56,070,624.0814 | -15,443,259.2263 | -21.59 |
| proxy_m3 | m3/yr | 47,463,455.7923 | 62,906,715.0186 | 15,443,259.2263 | 32.54 |
| proxy_share_of_assigned | share | 0.3989 | 0.5287 | 0.1298 | 32.54 |
| facilities_used | count | 208.0000 | 203.0000 | -5.0000 | -2.40 |
| assignments | count | 208.0000 | 203.0000 | -5.0000 | -2.40 |
| mean_road_distance_km | km | 558.5362 | 521.9717 | -36.5644 | -6.55 |
| max_road_distance_km | km | 1,527.0252 | 1,462.4581 | -64.5671 | -4.23 |
| median_road_distance_km | km | 542.2725 | 445.1758 | -97.0966 | -17.91 |
| total_volume_distance_m3_km | m3*km/yr | 66,453,145,604.5717 | 62,102,809,691.2193 | -4,350,335,913.3524 | -6.55 |
| transport_cost_cad | CAD/yr | 6,816,930,869.2006 | 6,382,487,942.4042 | -434,442,926.7964 | -6.37 |
| transport_cost_cad_m3 | CAD/m3 | 57.2960 | 53.6446 | -3.6515 | -6.37 |
| transport_cost_cad_gj | CAD/GJ | 14.0777 | 13.1805 | -0.8972 | -6.37 |
| binding_facilities | count | 196.0000 | 191.0000 | -5.0000 | -2.55 |
| binding_volume_m3 | m3/yr | 111,230,948.3372 | 112,335,799.3045 | 1,104,850.9673 | 0.99 |
| used_facility_utilization | share | 0.9471 | 0.9619 | 0.0148 | 1.56 |
| hhi | index_0_1 | 0.0129 | 0.0131 | 0.0003 | 2.10 |
| top5_share | share | 0.1575 | 0.1553 | -0.0022 | -1.40 |

### Local-preference sensitivity

| Penalty km | Penalty CAD/m3 | Cross share | Mean km | Cost CAD | CAD/GJ | Proxy share |
|---|---|---|---|---|---|---|
| 0 | 0.00 | 0.0790 | 506.3 | 6,196,584,308 | 12.797 | 0.5897 |
| 250 | 26.48 | 0.0264 | 512.3 | 6,268,033,610 | 12.944 | 0.5528 |
| 500 | 51.45 | 0.0003 | 522.0 | 6,382,487,942 | 13.180 | 0.5287 |
| 1,000 | 101.38 | 0.0003 | 522.0 | 6,382,487,942 | 13.180 | 0.5287 |

## 4. Uneconomic facilities and distance

The table below is a **transport-only** face-value screen. It is not a policy, investment, or official OSeCAN statement. A positive flag means modelled transport cost alone exceeds the tier face value before any feedstock, processing, or conversion cost is added.

- **T1**: 188 facilities, 112,240,750 m3/yr (0.9434 of assigned volume) have facility-weighted mean transport-only cost above the tier.
- **T2**: 188 facilities, 112,240,750 m3/yr (0.9434 of assigned volume) have facility-weighted mean transport-only cost above the tier.
- **T3**: 183 facilities, 109,950,490 m3/yr (0.9241 of assigned volume) have facility-weighted mean transport-only cost above the tier.
- **T4**: 183 facilities, 109,950,490 m3/yr (0.9241 of assigned volume) have facility-weighted mean transport-only cost above the tier.

### Highest transport-only cost facilities (v8 primary)

| Facility | Province | Class | m3/yr | Mean km | CAD/GJ | Above T4 |
|---|---|---|---|---|---|---|
| G.D.S. Énergie inc. | QC | PELLET | 325,998 | 1,527.0 | 37.841 | true |
| GDS Énergie | QC | PELLET | 153,846 | 1,526.8 | 37.837 | true |
| Groupe Lebel - Cacouna | QC | PELLET | 153,846 | 1,522.2 | 37.723 | true |
| Groupe Lebel inc. (Lebel Énergie) | QC | PELLET | 307,050 | 1,520.2 | 37.673 | true |
| Scierie de la Vallée | QC | SAW | 42,900 | 1,503.2 | 37.256 | true |
| Scierie SerDam | QC | SAW | 53,000 | 1,485.0 | 36.811 | true |
| Bois Marsoui G.D.S. inc. (Marsoui) | QC | SAW | 242,000 | 1,479.9 | 36.686 | true |
| Charbon de Bois Franc Basques inc. | QC | BIO | 22,000 | 1,476.1 | 36.591 | true |
| Uniboard Canada Inc | QC | PANEL | 950,000 | 1,476.0 | 36.590 | true |
| Kraft Nordic S.E.C. (pâtes et papiers) | QC | PULP | 1,575,000 | 1,462.5 | 36.257 | true |

- Facilities with transport-only cost below the lowest face-value tier (T1): **20**. This short-haul tail is the only part of the v8 assignment that is not above T1 on transport alone.
- The v9 facility set is included in `v9_facility_transport_cost.csv`; its tier flags are computed with the same threshold and should be read with the same caveat.

## 5. Validation

- `v8_cost_arithmetic`: true
- `v8_conservation`: true
- `v9_conservation`: true
- `v9_local_plus_cross_equals_assigned`: true
- `v9_capacity_bounds`: true
- `v9_local_first_shortfall_only`: true
- `province_reconciliation`: true
- `comparison_arithmetic`: true
- `v9_transport_cost_below_v8`: true
- `v9_mean_distance_below_v8`: true
- `products_residue_unchanged`: true
- `tier_flags_well_formed`: true
- `sensitivity_cost_order`: true
- `no_nan_or_negative`: true
- `utilization_complete`: true
- `labels`: true

## 6. Caveats

- Road distances are the v8 province-factor screening distances, not observed routes for every origin-facility pair.
- The 52.5 m3 base payload and empty return are the transport v1 base assumptions; low/high cost columns bound cost parameters only, not route or payload choice.
- The transport cost covers trucking only. It excludes feedstock, processing, conversion, handling, and storage costs.
- Tier comparison uses face-value adopted supply-curve tiers with no currency or price-year conversion; see the tier caveat.
- V9 is a screening LP with finite facility capacities and a soft local preference. It is not a market equilibrium, procurement plan, or policy recommendation.
- V9 uses more proxy-capacity facilities than v8; the proxy share is reported so the evidence trade-off is explicit.
- Products and residue are unchanged in model definitions; no product/residue artifact is written by this run.

## 7. Reproduce

`.venv/bin/python -m workflows.national.facilities.national_facility_assignment_v9`

