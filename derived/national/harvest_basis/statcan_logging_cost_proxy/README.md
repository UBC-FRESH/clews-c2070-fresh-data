# Provincial logging-industry cost proxy (StatCan 16-10-0114-01)

**Status:** industry aggregate proxy. Every row is `evidence=industry_aggregate_proxy`, `observation_type=industry_aggregate_proxy`, `not_logging_haul_breakdown=true`, `observed=false`, and `policy_grade=false`. This is **not** an observed logging cost, a logging cost curve, a haul-cost estimate, or a policy-grade value.

## Source and method

- Numerator: Statistics Canada Table 16-10-0114-01, NAICS 11331 (`Logging`), latest reference year 2024 (preliminary). Values are converted from thousands of dollars to nominal 2024 CAD.
- Denominator: `data/derived/national/harvest_basis/provincial_allocation/119m.csv` `observed_2024_m3` (2024 observed provincial harvest). The `harvest_m3` column from the same file is a 119 Mm3 scenario allocation and is reported only as a sensitivity.
- `industry_expense_cad_m3 = total_expenses_cad / harvest_m3`.
- Component shares use total expenses as the denominator. The remaining share is `other_expense_share` (administration, depreciation, overhead, and other unpriced costs).
- Contract logging (NAICS 113312) is reported separately against the same harvest denominator; it is not added to the NAICS 11331 total.

## Values by province

| Province | Harvest 2024 (Mm3) | Total expenses (M CAD) | Aggregate (CAD/m3) | Salaries % | Materials % | Energy % | Other % | Status |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| BC | 38.877 | 5,455.1 | 140.32 | 14.0% | 53.5% | 7.1% | 25.4% | available |
| AB | 22.260 | 1,224.0 | 54.99 | 20.4% | 49.5% | 11.0% | 19.1% | available |
| SK | 4.225 | 153.9 | 36.42 | 16.1% | 52.7% | 12.5% | 18.7% | available |
| MB | 1.104 | 58.4 | 52.87 | 23.6% | 36.8% | 17.4% | 22.2% | available |
| ON | 13.122 | 1,098.7 | 83.73 | 15.4% | 53.8% | 10.3% | 20.4% | available |
| QC | 25.939 | 2,626.8 | 101.27 | 15.2% | 52.8% | 7.9% | 24.1% | available |
| NB | 9.341 | 921.7 | 98.67 | 12.8% | 35.5% | 10.1% | 41.7% | available |
| NS | 2.322 | 91.8 | 39.52 | 24.7% | 27.9% | 18.9% | 28.5% | available |
| NL | 1.414 | 51.1 | 36.12 | 33.9% | 17.4% | 15.6% | 33.2% | available |
| PE | 0.294 | 13.3 | 45.17 | 18.0% | 30.6% | 13.3% | 38.1% | available |
| YT | 0.043 | 1.0 | 24.18 | 16.8% | 41.6% | 8.7% | 32.8% | available |
| NT | 0.037 | 0.2 | 4.59 | 16.7% | 43.5% | 8.9% | 31.0% | available |
| NU | 0.000 | 0.0 | — | — | — | — | — | undefined_zero_harvest_denominator |

National context: Canada NAICS 11331 total expenses 11695849000 CAD over 118977339 m3 = 98.303165 CAD/m3. Canada is context only; provincial rows are the deliverable.

## Contract logging (NAICS 113312), same harvest denominator

| Province | Total expenses (M CAD) | Aggregate (CAD/m3) | Status |
|---|---:|---:|---|
| BC | 2,467.3 | 63.46 | available |
| AB | 895.5 | 40.23 | available |
| SK | 78.1 | 18.49 | available |
| MB | 40.7 | 36.85 | available |
| ON | 525.2 | 40.02 | available |
| QC | 1,373.2 | 52.94 | available |
| NB | 226.5 | 24.24 | available |
| NS | 51.3 | 22.07 | available |
| NL | 46.5 | 32.90 | available |
| PE | 5.2 | 17.66 | available |
| YT | — | — | suppressed |
| NT | — | — | suppressed |
| NU | 0.0 | — | undefined_zero_harvest_denominator |

## Coverage

- Expected jurisdictions: 13; present: 13.
- Available industry proxies: 12.
- Missing or undefined: NU.
- Blank cells mean missing/undefined, never zero-filled. Nunavut has a reported zero expense and zero harvest denominator, so its CAD/m3 is blank.
- Yukon, Northwest Territories, and Nunavut contract logging 2024 cells are suppressed (`x`) or unavailable; blank, not zero.

## Caveats

- **industry_aggregate_not_logging_or_haul_cost**: Total expenses are a NAICS 11331 establishment aggregate. They include administration, depreciation, overhead, non-logging activity and any in-forest log hauling performed by logging establishments; the table does not publish a logging-only or haul-only cost.
- **double_counting_with_contract_and_haul_models**: Do not add this aggregate to a separate truck-haul or silviculture cost without checking overlap. NAICS 11331 is the parent of 113311 and 113312; summing both child industries would double count. Payments from 113311 establishments to 113312 contractors may also appear in materials/supplies, creating intra-industry subcontract double counting at the parent level.
- **survey_coverage_bias**: The Annual Survey of Manufacturing and Logging Industries covers employer establishments. Non-employer contractors, owner-operators and community or informal harvest are not fully represented, while the harvest denominator includes all provincial harvest. This can bias CAD/m3 downward, especially in the territories.
- **year_and_price_basis**: Expenses are reference year 2024, the latest year in the 2025-12-18 table release, and are preliminary and subject to revision. Values are nominal 2024 CAD; no deflator or escalation is applied. The primary harvest denominator is the 2024 observed provincial harvest in provincial_allocation/119m.csv. The 119 Mm3 allocation column is a scenario basis: it introduces a year/scenario mismatch and is reported only as a sensitivity, not as the primary ratio.
- **harvest_denominator_choice**: Observed 2024 harvest is used because it includes Crown and private volume and aligns with the establishment coverage of the expense numerator. The 119 Mm3 allocation is capped by Crown AAC in some provinces; for New Brunswick it is 6.23 Mm3 versus 9.34 Mm3 observed, which would inflate the scenario ratio to about 148 CAD/m3. Both ratios are published for transparency.
- **component_detail**: Only four expense components are published: total salaries and wages, materials and supplies, total energy/water utility/vehicle fuel, and an unpriced residual. Since reference year 2022 the energy, water and vehicle-fuel detail is no longer published. Shares use total expenses as the denominator.
- **quality_symbols**: Statistics Canada quality symbols are preserved: A/B/C/D/E are published estimates (D means acceptable, E use with caution), F is too unreliable, and x is suppressed. D is a data-quality flag, not a deletion. Suppressed or unavailable cells are blank, never zero-filled. Nunavut has a reported zero expense and zero harvest denominator, so its CAD/m3 is undefined and left blank.
- **jurisdiction_aggregation**: Only the 13 individual provinces and territories are used. Statistics Canada Atlantic Region and Prairie Region rows are aggregates and are excluded to avoid double counting. Canada is used only as national context.

## Files

- `provincial_logging_cost_proxy.csv`: 13 jurisdiction rows.
- `sources.csv`: source register with hashes and licence.
- `summary.json`: machine-readable values, coverage, and caveats.
- `manifest.json`: artifact provenance and output hashes.

## Reproduce

```bash
.venv/bin/python -m workflows.national.harvest.statcan_logging_cost_proxy
```
