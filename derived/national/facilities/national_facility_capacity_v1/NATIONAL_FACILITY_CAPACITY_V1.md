# National Facility Capacity v1

Generated 2026-11-22T20:29:43+00:00.

**Labels:** `model_estimate`; `observed=false`; `policy_grade=false`.

Scope: one capacity row per national facility inventory v0 record. Published capacities are carried unchanged. Blank relevant-class records receive a BC class-median proxy with a p25-p75 range. No facility measurement is invented and no legal/AAC claim is made.

## Method

1. Carry every published inventory capacity unchanged (179 records).
2. Compute the median BC published capacity for each relevant facility class (SAW, PULP, PANEL, PELLET, BIO).
3. Apply that class median to blank records of the same class (292 records). Label them `capacity_status=proxy`, `capacity_evidence=class_median_proxy`, `not_published` in the source data, and report p25-p75.
4. Leave a class without a BC anchor blank (15 OTHER records).
5. Do not scale by provincial harvest share. No documented per-class provincial scaling exists, so `province_scale=1`.

## Published versus proxy capacity

| Class | Records | Published | Proxy | Unavailable | Published m3/yr | Proxy m3/yr |
|---|---|---|---|---|---|---|
| SAW | 363 | 121 | 242 | 0 | 45,178,430 | 57,153,382 |
| PULP | 45 | 16 | 29 | 0 | 31,258,685 | 52,097,804 |
| PANEL | 22 | 17 | 5 | 0 | 4,215,736 | 1,069,200 |
| PELLET | 14 | 13 | 1 | 0 | 6,859,300 | 574,000 |
| BIO | 27 | 12 | 15 | 0 | 8,326,259 | 9,346,200 |
| OTHER | 15 | 0 | 0 | 15 | 0 | 0 |

Published capacity total: **95,838,409 m3/yr**. Proxy capacity total: **120,240,586 m3/yr** (55.6% of the combined total).

## BC anchor distribution

| Class | BC records | Min m3/yr | p25 m3/yr | Median m3/yr | p75 m3/yr | Max m3/yr |
|---|---|---|---|---|---|---|
| SAW | 121 | 1,233 | 25,250 | 236,171 | 686,145 | 1,822,248 |
| PULP | 16 | 484,425 | 1,021,943 | 1,796,476 | 3,045,773 | 3,498,280 |
| PANEL | 17 | 1,124 | 116,711 | 213,840 | 340,414 | 837,334 |
| PELLET | 13 | 86,100 | 251,125 | 574,000 | 662,970 | 1,257,060 |
| BIO | 12 | 15,875 | 358,172 | 623,080 | 908,824 | 2,162,923 |

Quantiles use linear interpolation (R-7) and are rounded to whole m3/yr. The median is the proxy point value; p25 and p75 are the reported proxy range.

## Province and class totals

| Province | Records | Published | Proxy | Unavailable | Total m3/yr |
|---|---|---|---|---|---|
| BC | 274 | 179 | 87 | 8 | 130,779,940 |
| AB | 15 | 0 | 15 | 0 | 5,832,026 |
| SK | 3 | 0 | 3 | 0 | 708,513 |
| MB | 3 | 0 | 3 | 0 | 708,513 |
| ON | 29 | 0 | 28 | 1 | 9,333,820 |
| QC | 111 | 0 | 106 | 5 | 44,824,771 |
| NB | 19 | 0 | 19 | 0 | 9,168,164 |
| NS | 18 | 0 | 18 | 0 | 10,092,720 |
| PE | 2 | 0 | 2 | 0 | 472,342 |
| NL | 11 | 0 | 10 | 1 | 3,922,015 |
| YT | 1 | 0 | 1 | 0 | 236,171 |
| NT | 0 | 0 | 0 | 0 | 0 |
| NU | 0 | 0 | 0 | 0 | 0 |

## Public sources screened

| Source | Access | Used | Licence / note |
|---|---|---|---|
| bc_mills_db_2015 | available | yes_published_anchor | Project-derived BC chain layer; upstream ISED Mills DB 2015 / FFCM proxies. Upstream source is not relicensed here. |
| class_median_proxy_v1 | computed | yes_proxy | Model-derived proxy. Anchor values inherit the BC Mills DB / FFCM lineage; not a facility measurement and not relicensed. |
| canadian_biomass_pellet_map_2025 | available_not_adopted | no | Public PDF, copyright Annex Business Media. Factual capacity figures referenced for cross-check only; not redistributed. |
| alberta_forest_products_members | available_not_adopted | no | Public website; factual member listing, all rights reserved |
| fpac_member_mills | http_404 | no | Public website; all rights reserved |
| ofia_members | http_403 | no | Public website; all rights reserved |

The Canadian Biomass pellet map is directly accessible and public, but its capacity unit is finished pellet tonnes/yr. Converting it to infeed m3/yr would require an unpublished conversion and 42 of its 43 plants are absent from inventory v0, so it is recorded as a cross-check source only. No restricted or proprietary data are used.

## Caveats

- All volumes are model estimates (`model_estimate`); `observed=false` and `policy_grade=false`.
- Published capacity is the 2015 Mills DB/FFCM processing-line infeed proxy carried by national_facility_inventory_v0, not licensed, current, or verified operating capacity.
- Class-median proxies are statistical placeholders, not facility measurements. They are labelled `class_median_proxy` and `not_published`; their p25-p75 range is reported.
- The anchor distribution is BC-only. Applying BC class medians to other provinces assumes comparable class structure; that assumption is untested and is a first-order uncertainty.
- No provincial scaling is applied. A province's harvest share does not change its facility proxy capacity in v1.
- OTHER-class records have no BC published anchor and are left blank. They are excluded from assignment v2 rather than given an invented capacity.
- The Canadian Biomass pellet map is public but reports finished pellet tonnes/yr, not infeed m3/yr; it was not adopted. No restricted or proprietary data are used.
- These capacities are planning inputs only. They are not a legal/AAC determination, a timber-supply approval, or an observed operating capacity.
- No UI or public OSeCAN surface is changed by this artifact.

## Verification

```bash
.venv/bin/python -m workflows.national.facilities.national_facility_capacity
.venv/bin/pytest tests/test_national_facility_capacity.py
.venv/bin/ruff check workflows/national/facilities/national_facility_capacity.py tests/test_national_facility_capacity.py
```
