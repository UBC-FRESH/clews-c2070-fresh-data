# National Evidence-Tier Coverage and Replacement Queue

Status: **model estimate scaffold audit — not policy grade, not observed.** Generated 2026-11-22T06:10:05+00:00.

## 1. Scope

All **13 provinces and territories** are covered at **5 components** each (price, logging, haul, road, silviculture): **65 of 65** coverage cells. There are **0 silent gaps**.

This audit does not recalculate prices, costs or margins. Logging and haul are separate coverage cells because the parent scaffold exposes them as one combined distribution; no logging/haul split is invented.

## 2. Tier counts and shares

| Tier | Score | Cells | Cell share | Volume-weighted share |
|---|---:|---:|---:|---:|
| `reported_average` | 4 | 3 | 0.0462 | 0.1792 |
| `proxy_model` | 3 | 2 | 0.0308 | 0.1344 |
| `donor_proxy` | 2 | 60 | 0.9231 | 0.6863 |
| `assumption` | 1 | 0 | 0.0000 | 0.0000 |

`reported_average` is the only tier counted as direct/reported provincial evidence. `proxy_model` remains a model, `donor_proxy` remains a donor, and assumptions remain named assumptions.

### Component detail

| Component | reported_average | proxy_model | donor_proxy | assumption |
|---|---:|---:|---:|---:|
| price | 1 | 0 | 12 | 0 |
| logging | 0 | 1 | 12 | 0 |
| haul | 0 | 1 | 12 | 0 |
| road | 1 | 0 | 12 | 0 |
| silviculture | 1 | 0 | 12 | 0 |

## 3. Volume-weighted coverage

- National allocation volume: **118,977,339.1 m3/yr**.
- Volume-weighted direct/reported share: **0.1792** (17.92%).
- Volume-weighted proxy-model share: **0.1344**.
- Volume-weighted donor/assumption share: **0.6863**.
- Volume-weighted tier score (0–4): **2.4929**.
- Volume-weighted evidence ratio: **0.6232**.

The denominator is five equally weighted components per province. Direct/reported volume therefore counts only `reported_average` cells; it is not inflated by donor or proxy cells.

## 4. Donor provenance

Donor provinces: **BC, QC**.

| Donor | Cells | Price | Logging | Haul | Road | Silviculture |
|---|---:|---:|---:|---:|---:|---:|
| BC | 48 | 12 | 12 | 12 | 0 | 12 |
| QC | 12 | 0 | 0 | 0 | 12 | 0 |

BC is the price, logging+haul and silviculture donor. QC is the road donor. A donor value is never relabelled as the recipient's own evidence.

## 5. Source-replacement queue

**60 donor/assumption rows** are queued by provincial harvest volume. Priority thresholds: P1 ≥10% of national volume, P2 ≥2%, P3 >0%, P4 zero volume.

| Priority | Rows |
|---|---:|
| P1 | 15 |
| P2 | 15 |
| P3 | 25 |
| P4 | 5 |

| Required source category | Rows |
|---|---:|
| cost study | 24 |
| price series | 12 |
| road/silviculture rate | 24 |

First rows:

| Rank | Priority | Province | Component | Tier | Required source | Volume (m3) |
|---:|---|---|---|---|---|---:|
| 1 | P1 | BC | road | `donor_proxy` | road/silviculture rate | 39,978,577 |
| 2 | P1 | QC | price | `donor_proxy` | price series | 26,674,334 |
| 3 | P1 | QC | logging | `donor_proxy` | cost study | 26,674,334 |
| 4 | P1 | QC | haul | `donor_proxy` | cost study | 26,674,334 |
| 5 | P1 | QC | silviculture | `donor_proxy` | road/silviculture rate | 26,674,334 |
| 6 | P1 | AB | price | `donor_proxy` | price series | 22,891,404 |
| 7 | P1 | AB | logging | `donor_proxy` | cost study | 22,891,404 |
| 8 | P1 | AB | haul | `donor_proxy` | cost study | 22,891,404 |
| 9 | P1 | AB | road | `donor_proxy` | road/silviculture rate | 22,891,404 |
| 10 | P1 | AB | silviculture | `donor_proxy` | road/silviculture rate | 22,891,404 |
| 11 | P1 | ON | price | `donor_proxy` | price series | 13,493,596 |
| 12 | P1 | ON | logging | `donor_proxy` | cost study | 13,493,596 |
| 13 | P1 | ON | haul | `donor_proxy` | cost study | 13,493,596 |
| 14 | P1 | ON | road | `donor_proxy` | road/silviculture rate | 13,493,596 |
| 15 | P1 | ON | silviculture | `donor_proxy` | road/silviculture rate | 13,493,596 |

The full ranked queue is in `source_replacement_queue.csv`. `proxy_model` cells are tracked as second-wave upgrades in the summary but are not mixed into the donor/assumption queue.

## 6. Fail-closed and labels

- The builder halts on any unexpected `D` in parent or `data` git status.
- All 13 jurisdictions and all five components are present; missing cells fail the build.
- `evidence=model_estimate`, `observed=false`, `policy_grade=false`, `net_value_status=model_estimate`, `combined_national_net_value=false`.
- The national total remains `model_estimate_not_policy`.
- No new margin arithmetic is performed.

## 7. Reproduction

```bash
.venv/bin/python -m workflows.national.harvest.national_tier_coverage
```
