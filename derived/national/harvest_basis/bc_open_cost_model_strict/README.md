# Strict-open BC logging and truck-haul cost model

**Status:** strict-open proxy model. Every estimate, comparison, sensitivity
and summary row carries `evidence=model_estimate`,
`cost_basis=strict_open_proxy`, `licence_tier=strict_open`,
`policy_grade=false`, `observed=false`. The source register also carries
`licence_tier=strict_open` at row level and the actual source licence in
`source_licence_tier`; that column is the proof of the strict-open claim. This
is **not** an observed contractor cost, a mill settlement, or a BC empirically
calibrated model.

## Licence rule

Only four input families are used:

1. Statistics Canada Open Licence aggregate tables (wages, diesel, CPI,
   machinery/equipment price index, trucking freight index, logging-industry
   aggregates).
2. Open Government Licence - Canada derived terrain and road aggregates
   (NRCan MRDEM-30 slope screen, National Road Network).
3. Open Government Licence - British Columbia derived forest-inventory
   aggregates (BC VRI 2025 area/species/THLB table).
4. CC BY 4.0 or public-domain methods: Sessions, Berry & Han (2021) and
   Miyata (1980). OSM ODbL was not needed and is not used.

Excluded and **not read**: IAM/CAM appraisal manuals, the TLA/ILA/NWLA/MNP
rate guide, FPInnovations/FERIC reports, BCWS rates, any Crown-copyright PDF,
and proprietary or restricted data/microdata. The only non-strict-open file
read is the existing public-reference model's output CSV, and that is used
solely for the cross-check table; it is not a model input.

## Equations

Machine rate per productive machine hour (PMH), following Miyata (1980) and
the utilization-adjusted life of Sessions, Berry & Han (2021):

```
D        = (P - S) / (life_years * annual_PMH)
AVI      = P - (P - S) * (life_years - 1) / (2 * life_years)
interest = (i + insurance_tax_storage) * AVI / annual_PMH
fuel     = litres_per_PMH * diesel_CAD_per_litre * (1 + lube_fraction)
repair   = repair_fraction * D
tires    = tire_fraction * D
labour   = wage_CAD_per_SMH * (1 + burden) / utilization
PMH_cost = (D + interest + fuel + repair + tires + labour) * (1 + overhead)
SMH_cost = PMH_cost * utilization
```

`modified` method: `life_years = economic_life_hours / (SMH_per_year * U)`.
`traditional` method: `life_years = economic_life_hours / SMH_per_year`.
The base case uses `modified`; the `traditional` method is retained only for
the Sessions et al. worked-example check.

Logging:

```
phase_cost = machine_rate_CAD_per_PMH / productivity_m3_per_PMH
logging    = sum(phase costs) * (1 + support) + mobilization / sale_volume + planning
```

Productivity is an explicit engineering cycle-time estimate:

```
felling    = piece * 3600 / (14 + 26 * piece) * 0.80
skidder    = min(7, 4 + 4 * piece) / (0.24 - 0.06 * min(piece,1)) * 0.85
processor  = piece * 3600 / (16 + 30 * piece) * 0.80
yarder     = min(6, 3.5 + 3 * piece) / (0.16 - 0.03 * min(piece,1)) * 0.75
loader     = 2.2 / 0.025 * 0.90
```

Ground slope factor `1/(1 + 0.018 * max(0, slope-10))`; cable slope factor
`1/(1 + 0.010 * max(0, slope-35))`. These are engineering proxies, not BC
cost elasticities.

Truck haul:

```
CYCLE = 1 km in-block loaded/empty + road km loaded/empty
        + delay hours + load/unload hours
haul  = (truck_PMH + trailer_PMH) * CYCLE / payload * (1 + haul_support)
```

## Explicit assumptions

| Item | Base assumption | Range |
|---|---|---|
| Capital price | 2017 replacement-price assumption x MEPI 2026/100 | -15% / +20% |
| Machine utilization | 65-85% by machine, region-adjusted | -10 / +5 percentage points |
| Machine life | 12,000-15,000 PMH | -15% / +20% |
| Diesel | StatCan Vancouver 12-month mean | 12-month min/max |
| Wage | midpoint of StatCan logging production-worker and BC forestry anchors | StatCan natural-resource production / BC forestry |
| Payload | 50 m3 per truck trip | 42-55 m3 |
| Road speed | 55 km/h loaded, 65 km/h empty | 45-60 / 55-70 km/h |
| Delay/load | 1.30 h delay + 0.50 h load/unload | 1.00-1.50 h / 0.40-0.60 h |
| Overhead/profit | 15% | 10-20% |

The capital price is a stated 2017 assumption escalated by the Statistics
Canada MEPI for logging/construction/mining machinery. It is not a dealer
quote. The 2,000 paid hours per year used to convert annual logging wages to
an hourly rate is the Miyata (1980) scheduled-time convention, not a BC payroll
observation.

The low and high columns stack favourable or unfavourable parameter draws
(capital, utilization, productivity, diesel, wage, overhead and haul cycle).
They are a **stress envelope**, not a statistical confidence interval and not a
probability statement.

## Coverage

- 7 BC forest zones: 1 Coast, 6 Interior.
- 4 slope classes: 10%, 25%, 40%, 55%; ground for 10/25, cable for 40/55.
- 3 piece sizes: 0.30, 0.60, 1.00 m3/tree.
- 3 sale volumes: 5,000, 20,000, 100,000 m3.
- 3 haul distances: 50, 100, 150 km.
- 756 estimate rows.

Regional slope weights are computed from the OGL-Canada MRDEM-30 derived
slope screen and OGL-BC VRI forest area by ecoprovince. The >30% slope area is
split 90/10 between the steep and very-steep classes; that split is an
assumption because the open aggregate publishes only the >15% and >30%
thresholds.

Zone is an administrative label in this model. No strict-open BCTS-zone cost
or inventory crosswalk was identified, so the six Interior zones share the
same regional parameters and differ only by label; the meaningful cost split
is Coast versus Interior. The row-level grid still covers every zone label so
it can be joined to other administrative tables without inventing a crosswalk.

## Worked examples (recomputed in the build)

| Check | Expected CAD/PMH | Computed CAD/PMH |
|---|---:|---:|
| sessions_2021_100pct | 140.60 | 140.60 |
| sessions_2021_50pct_traditional | 269.20 | 269.20 |
| sessions_2021_50pct_modified | 192.60 | 192.60 |
| miyata_1980_example_11 | 35.61 | 35.61 |

The Sessions et al. examples reproduce 140.60 at 100% utilization, 269.20 for
the traditional method at 50%, and 192.60 for the modified method at 50%. The
Miyata Example 11 reproduces 35.61/PMH.

## Cost estimates

{
  "total_base_median_cad_m3": 64.94,
  "total_base_min_cad_m3": 40.22,
  "total_base_max_cad_m3": 105.2,
  "by_region": {
    "Coast": {
      "median_total_base_cad_m3": 69.16,
      "min_total_base_cad_m3": 43.19,
      "max_total_base_cad_m3": 105.2
    },
    "Interior": {
      "median_total_base_cad_m3": 64.52,
      "min_total_base_cad_m3": 40.22,
      "max_total_base_cad_m3": 98.0
    }
  },
  "by_system": {
    "ground": {
      "median_total_base_cad_m3": 59.0,
      "min_total_base_cad_m3": 40.22,
      "max_total_base_cad_m3": 86.07
    },
    "cable": {
      "median_total_base_cad_m3": 72.51,
      "min_total_base_cad_m3": 49.79,
      "max_total_base_cad_m3": 105.2
    }
  }
}

## Comparison to the public-reference model

The existing public-reference model is used **only** as a cross-check. Its
rates and coefficients are not inputs to this model. 756 overlapping scenarios were matched; the median strict/reference ratio is 1.208 and the median delta is +11.21 CAD/m3. This is a cross-check, not calibration and not an input.

The comparison file records the delta and ratio for every overlapping
scenario. A positive delta means the strict-open model is higher. Differences
are expected because the reference model uses different machine rates,
productivity sources, and appraisal-manual coefficients.

## Is a strict-open BC price series still needed?

**Yes.** This model supplies only the cost side. The existing BC log-market
price reports are public-reference Crown-copyright material, not strict-open
data. Statistics Canada does not publish a BC delivered-log price series. A
strict-open net-value calculation therefore still needs an OGL-BC or CC-BY
released BC delivered-log price series (or a public-domain equivalent). Until
that exists, this model can support a strict-open **cost** estimate only, not a
strict-open net value or margin.

## Files

| File | Rows | Purpose |
|---|---:|---|
| `strict_estimates.csv` | 756 | Zone x slope x piece x volume x distance low/base/high |
| `strict_region_slope.csv` | 8 | Region x slope representative costs and OGL slope weights |
| `strict_zone_summary.csv` | 7 | Area-weighted slope expectation by zone |
| `strict_sensitivity.csv` | 22 | One-at-a-time sensitivity cases |
| `strict_parameters.csv` | 56 | Equations, assumptions, units, ranges, sources |
| `strict_sources.csv` | 14 | Source and licence register |
| `strict_statcan_observations.csv` | 56 | Frozen public statistics used by the build |
| `strict_worked_examples.csv` | 4 | Recomputed Miyata/Sessions examples |
| `strict_comparison.csv` | 756 | Row-level cross-check versus the public-reference model |
| `strict_comparison_summary.csv` | 14 | Cross-check summary by zone/system |
| `manifest.json` | - | Inputs, hashes, validation, limitations, non-claims |
| `summary.json` | - | Compact summary and strict-open price-series gap |

## Source register

| Source key | Title | Licence | Tier |
|---|---|---|---|
| `model_assumptions_cc0` | Explicit engineering assumptions of the strict-open BC cost model | CC0 1.0 Universal public-domain dedication | `public_domain` |
| `statcan_18100004_cpi` | Consumer Price Index, monthly, not seasonally adjusted (Table 18-10-0004-01) | Statistics Canada Open Licence | `statcan_open` |
| `statcan_18100001_diesel` | Monthly average retail prices for gasoline and fuel oil, by geography (Table 18-10-0001-01) | Statistics Canada Open Licence | `statcan_open` |
| `statcan_14100064_wages_industry` | Employee wages by industry, annual (Table 14-10-0064-01) | Statistics Canada Open Licence | `statcan_open` |
| `statcan_14100417_wages_occupation` | Employee wages by occupation, annual (Table 14-10-0417-01) | Statistics Canada Open Licence | `statcan_open` |
| `statcan_16100114_logging_industry` | Logging industries, principal statistics by North American Industry Classification System (Table 16-10-0114-01) | Statistics Canada Open Licence | `statcan_open` |
| `statcan_18100283_mepi_commodity` | Machinery and equipment price index, by commodity, monthly (Table 18-10-0283-01) | Statistics Canada Open Licence | `statcan_open` |
| `statcan_18100284_mepi_industry` | Machinery and equipment price index, by industry of purchase, monthly (Table 18-10-0284-01) | Statistics Canada Open Licence | `statcan_open` |
| `statcan_18100281_trucking_ppi` | For-hire motor carrier freight services price index, monthly (Table 18-10-0281-01) | Statistics Canada Open Licence | `statcan_open` |
| `bc_vri_2025_area_weights` | BC VRI 2025 forest and THLB area weights (derived aggregate) | Open Government Licence - British Columbia 2.0 | `ogl_bc` |
| `nrcan_mrdem_30_slope` | NRCan MRDEM-30 terrain slope screen (derived 960 m aggregate) | Open Government Licence - Canada 2.0 | `ogl_canada` |
| `nrcan_nrn_bc_roads` | National Road Network, British Columbia (derived road-distance classes) | Open Government Licence - Canada 2.0 | `ogl_canada` |
| `sessions_berry_han_2021` | Machine rate estimates and equipment utilization - a modified approach | Creative Commons Attribution 4.0 International (CC BY 4.0) | `cc_by` |
| `miyata_1980` | Determining fixed and operating costs of logging equipment | Public domain (U.S. Government work) | `public_domain` |

Full URLs, retrieval timestamps, licence URLs and the exact use of every
source are in `strict_sources.csv` and `manifest.json`.

## Validation

- 756 estimate rows; no NaN, infinite or negative values.
- Every row satisfies `total_low <= total_base <= total_high`.
- All zones, regions, slope classes, piece classes, volume classes and
  distance classes are present.
- Every estimate row carries the five required labels and
  `bc_empirical_calibration=false`.
- The source register is scanned for forbidden restricted-source tokens.
- `manifest.json` records SHA-256 hashes for every derived input and output.
- The build fails closed on a missing input, a bad source licence tier, a
  non-finite or unordered cost, or a failed worked example.

## Non-claims and limitations

- Not an observed contractor cost, invoice, mill settlement, or profit.
- Not a BC empirical calibration; productivity and utilization are explicit
  engineering assumptions.
- Not policy grade; not a stumpage rate, AAC, tenure, or legal determination.
- No IAM/CAM, TLA/ILA/NWLA, FPInnovations, BCWS, Crown-copyright, proprietary
  or restricted input is used.
- The model covers tree-to-truck logging and general truck haul only. Road
  construction, bridges, silviculture, sorting, barge/rail and tenure costs are
  outside the boundary.
- Diesel is a retail pump price including taxes; this is a conservative fuel
  input.
