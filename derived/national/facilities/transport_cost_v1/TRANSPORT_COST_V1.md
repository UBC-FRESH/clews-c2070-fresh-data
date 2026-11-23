# National truck transport cost v1

Generated: 2026-11-23T14:08:17+00:00

Status: **model estimate**. Open-data bottom-up truck cost component; `model_estimate`, `observed=false`, `policy_grade=false`. No assignment change, no national observed claim, no policy claim, and no official OSeCAN or UI change.

## Cost components

Base trip at 100 km one-way and 52.5 m3 payload. The truck returns empty; every loaded kilometre is paired with an empty kilometre. Overhead is applied to the six operating components.

| Component | CAD/trip | CAD/m3 | Share of total | Basis |
|---|---|---|---|---|
| Fuel | 162.04 | 3.09 | 26.8% | StatCan diesel x L/km |
| Driver / labour | 230.43 | 4.39 | 38.2% | wage x burden x on-duty hours |
| Maintenance | 24.00 | 0.46 | 4.0% | repair and maintenance CAD/km |
| Tires | 12.00 | 0.23 | 2.0% | tire wear CAD/km |
| Capital | 81.56 | 1.55 | 13.5% | depreciation + interest on average investment |
| Insurance | 29.25 | 0.56 | 4.8% | annual insurance / productive km |
| Overhead | 64.71 | 1.23 | 10.7% | fraction of operating subtotal |
| **Total** | **604.00** | **11.50** | **100.0%** | |

## $/m3 vs distance

One-way road km; 52.5 m3 base payload; low/base/high is a favourable-to-unfavourable stress envelope, not a confidence interval.

| One-way km | Low CAD/m3 | Base CAD/m3 | High CAD/m3 | Base CAD/ODT | Base CAD/GJ |
|---|---|---|---|---|---|
| 50 | 3.78 | 6.51 | 11.11 | 29.60 | 1.60 |
| 100 | 6.84 | 11.50 | 19.29 | 52.29 | 2.83 |
| 150 | 9.91 | 16.50 | 27.48 | 74.99 | 4.05 |
| 300 | 19.09 | 31.48 | 52.03 | 143.08 | 7.73 |
| 500 | 31.34 | 51.45 | 84.77 | 233.87 | 12.64 |

### Payload sensitivity

| One-way km | 45 m3 CAD/m3 | 52.5 m3 CAD/m3 | 60 m3 CAD/m3 |
|---|---|---|---|
| 50 | 7.60 | 6.51 | 5.70 |
| 100 | 13.42 | 11.50 | 10.07 |
| 150 | 19.25 | 16.50 | 14.44 |
| 300 | 36.72 | 31.48 | 27.54 |
| 500 | 60.03 | 51.45 | 45.02 |

## Supply-curve comparison

The comparison is in $/GJ at face value: transport is 2026 CAD/GJ; the adopted OSeCAN tier values are loaded as `$/GJ` with no documented currency or price-year conversion. The JSON field is named `variable_cost_usd_per_gj`, so this is an explicit parity/undocumented-currency assumption, not an FX conversion. A CAD-stronger interpretation would raise the tier threshold and push the crossing distances outward.

Crossing distance is the one-way road distance at which transport alone equals the tier variable cost, at 52.5 m3 base payload. Values above 1,000 km are outside the modelled range.

| Scenario | T1/T2 2.457 | T3 3.194 | T4 3.500 |
|---|---|---|---|
| low | 235.4 | 309.6 | 340.3 |
| base | 84.9 | 115.0 | 127.4 |
| high | 19.2 | 30.3 | 34.9 |

At the base payload and base cost, transport alone exceeds the T1/T2 adopted tier beyond the crossing shown, the T3 mid-cost tier beyond its crossing, and the T4 high-cost marginal tier beyond its crossing. At 50 km the base cost is below T1/T2; at 100 km it is above T1/T2 but below T3; at 150 km it is above T4. By 500 km every modelled scenario and payload exceeds all four tiers; at 300 km the most favourable low-cost, high-density, 60 m3 envelope is still below T3/T4. This is a screening statement about transport alone, not a delivered-cost or policy conclusion.

## Facility and road-distance context

- Assignment v6 has 742 rows / 366 unique facilities in 11 provinces.
- Recorded allocation distance quantiles (km): min 11.9, p25 256.1, median 653.3, p75 772.1, max 2501.7.
- Distance bins: le_50_km 15, gt_50_le_100_km 37, gt_100_le_150_km 43, gt_150_le_300_km 120, gt_300_le_500_km 78, gt_500_km 449.
- This is facility-to-province-centroid allocation distance, not a route; it is context only and changes no assignment.
- Road-distance audit v1 median road/haversine ratios range 1.320 to 2.643; curves use road km directly and do not apply a second factor.

## Parameters and sources

| Parameter | Unit | Low | Base | High | Source | Licence |
|---|---|---|---|---|---|---|
| `diesel_cad_per_l` | CAD/L | 1.6120 | 2.2506 | 2.8590 | Statistics Canada Table 18-10-0001-01: monthly average retail prices for gasoline and fuel oil | Statistics Canada Open Licence |
| `driver_wage_cad_per_h` | CAD/h | 29.1903 | 37.9566 | 50.0463 | Statistics Canada Table 14-10-0417-01: employee wages by occupation | Statistics Canada Open Licence |
| `payroll_burden_fraction` | fraction of wage | 0.2000 | 0.2500 | 0.3000 | Explicit engineering assumptions of transport cost v1 | CC0 1.0 Universal public-domain dedication |
| `payload_m3` | m3/trip | 45.0000 | 52.5000 | 60.0000 | Explicit engineering assumptions of transport cost v1 | CC0 1.0 Universal public-domain dedication |
| `residue_bulk_density_odt_per_m3` | ODT/m3 | 0.1500 | 0.2200 | 0.3000 | Explicit engineering assumptions of transport cost v1 | CC0 1.0 Universal public-domain dedication |
| `residue_lhv_gj_per_odt` | GJ/ODT | 16.4650 | 18.5000 | 20.5350 | National facility residue supply v7 summary | Project-derived; see source metadata |
| `moisture_content_wet_basis` | fraction | 0.4000 | 0.4500 | 0.5000 | Explicit engineering assumptions of transport cost v1 | CC0 1.0 Universal public-domain dedication |
| `fuel_loaded_l_per_km` | L/km | 0.3400 | 0.4000 | 0.4800 | Explicit engineering assumptions of transport cost v1 | CC0 1.0 Universal public-domain dedication |
| `fuel_empty_l_per_km` | L/km | 0.2700 | 0.3200 | 0.3800 | Explicit engineering assumptions of transport cost v1 | CC0 1.0 Universal public-domain dedication |
| `speed_loaded_kmh` | km/h | 45.0000 | 55.0000 | 65.0000 | Explicit engineering assumptions of transport cost v1 | CC0 1.0 Universal public-domain dedication |
| `speed_empty_kmh` | km/h | 55.0000 | 65.0000 | 70.0000 | Explicit engineering assumptions of transport cost v1 | CC0 1.0 Universal public-domain dedication |
| `terminal_hours_per_trip` | h/trip | 1.0000 | 1.5000 | 2.0000 | Explicit engineering assumptions of transport cost v1 | CC0 1.0 Universal public-domain dedication |
| `maintenance_cad_per_km` | CAD/km | 0.0800 | 0.1200 | 0.1600 | Explicit engineering assumptions of transport cost v1 | CC0 1.0 Universal public-domain dedication |
| `tire_cad_per_km` | CAD/km | 0.0400 | 0.0600 | 0.0800 | Explicit engineering assumptions of transport cost v1 | CC0 1.0 Universal public-domain dedication |
| `truck_capital_cad` | CAD | 301933.0000 | 355215.0000 | 426258.0000 | Strict-open BC logging and truck-haul cost model parameters | Project-derived; CC0 assumptions + Statistics Canada Open Licence observations |
| `economic_life_km` | km | 1000000.0000 | 1200000.0000 | 1400000.0000 | Explicit engineering assumptions of transport cost v1 | CC0 1.0 Universal public-domain dedication |
| `residual_value_fraction` | fraction of capital | 0.1000 | 0.1500 | 0.2000 | Explicit engineering assumptions of transport cost v1 | CC0 1.0 Universal public-domain dedication |
| `interest_rate` | fraction/year | 0.0500 | 0.0650 | 0.0800 | Explicit engineering assumptions of transport cost v1 | CC0 1.0 Universal public-domain dedication |
| `annual_km` | km/year | 100000.0000 | 100000.0000 | 100000.0000 | Explicit engineering assumptions of transport cost v1 | CC0 1.0 Universal public-domain dedication |
| `utilization_fraction` | fraction | 0.8000 | 0.8500 | 0.9000 | Explicit engineering assumptions of transport cost v1 | CC0 1.0 Universal public-domain dedication |
| `insurance_rate_of_capital_per_year` | fraction of capital/year | 0.0250 | 0.0350 | 0.0450 | Explicit engineering assumptions of transport cost v1 | CC0 1.0 Universal public-domain dedication |
| `overhead_fraction` | fraction of subtotal | 0.0800 | 0.1200 | 0.1800 | Explicit engineering assumptions of transport cost v1 | CC0 1.0 Universal public-domain dedication |
| `backhaul_fraction` | fraction of return km loaded | 0.0000 | 0.0000 | 0.0000 | Explicit engineering assumptions of transport cost v1 | CC0 1.0 Universal public-domain dedication |
| `legal_gvw_kg` | kg | 63500.0000 | 63500.0000 | 63500.0000 | Canadian Council of Motor Transport Administrators interprovincial weights and dimensions envelope | Public regulatory reference; not an open-data licence |
| `truck_tare_kg` | kg | 18000.0000 | 18000.0000 | 18000.0000 | Explicit engineering assumptions of transport cost v1 | CC0 1.0 Universal public-domain dedication |
| `legal_payload_kg` | kg | 45500.0000 | 45500.0000 | 45500.0000 | Parameter derived inside transport cost v1 | CC0 1.0 Universal public-domain dedication |
| `axle_limit_kg` | kg | 17000.0000 | 17000.0000 | 17000.0000 | Canadian Council of Motor Transport Administrators interprovincial weights and dimensions envelope | Public regulatory reference; not an open-data licence |
| `cpi_factor_2025_to_2026` | factor | 1.0289 | 1.0289 | 1.0289 | Statistics Canada Table 18-10-0004-01: consumer price index | Statistics Canada Open Licence |
| `freight_ppi_growth_2025_to_2026` | fraction | 0.0910 | 0.0910 | 0.0910 | Statistics Canada Table 18-10-0281-01: for-hire motor carrier freight services price index | Statistics Canada Open Licence |

## Method

```text
round_trip_km = 2 x one_way_km
driving_hours = one_way_km / speed_loaded + one_way_km / speed_empty
on_duty_hours = driving_hours + terminal_hours
fuel = diesel x one_way_km x (loaded_L_per_km + empty_L_per_km)
driver = wage x (1 + burden) x on_duty_hours
maintenance = maintenance_CAD_per_km x round_trip_km
tires = tire_CAD_per_km x round_trip_km
depreciation_per_km = capital x (1 - residual) / life_km
interest_per_km = capital x (1 + residual) / 2 x interest / (annual_km x utilization)
capital = (depreciation_per_km + interest_per_km) x round_trip_km
insurance = capital x insurance_rate / (annual_km x utilization) x round_trip_km
total = (fuel + driver + maintenance + tires + capital + insurance) x (1 + overhead)
CAD_per_m3 = total / payload_m3
CAD_per_ODT = total / (payload_m3 x bulk_density_ODT_per_m3)
CAD_per_GJ = CAD_per_ODT / LHV_GJ_per_ODT
CAD_per_ODT_km = CAD_per_ODT / one_way_km
```

## Limits

- This is a national-scope component, not a national observed average. The diesel price is the Vancouver self-service series; wages are BC anchors. No province-specific calibration is claimed.
- Bulk density, fuel burn, speeds, terminal time, life, residual, interest, insurance and overhead are engineering assumptions, not observations. The low/high columns stack favourable or unfavourable draws; they are not a statistical confidence interval.
- Mass is screened against a public 63,500 kg GVW / 45,500 kg payload envelope. The modelled residue loads are volume-limited; the mass cap is not binding in the stated density range. Axle-group limits are reported as context, not applied axle-by-axle.
- Empty return is modelled in full. No backhaul, border delay, customs, ferry, winter road, resource-road, queue at scale, or hours-of-service relay is costed. Trips over 13 on-duty hours are flagged.
- The supply-curve comparison treats the loaded tier $/GJ at face value. The interface does not document currency or price year; no FX or deflator is applied.
- No assignment, facility capacity, harvest, AAC, tenure, market, emissions, legal, or operating-status claim is made. No UI or official OSeCAN input is changed.

## Provenance

- Statistics Canada Table 18-10-0001-01: monthly average retail prices for gasoline and fuel oil: `data/derived/national/harvest_basis/bc_open_cost_model_strict/strict_statcan_observations.csv` (Statistics Canada Open Licence); `https://doi.org/10.25318/1810000101-eng`
- Statistics Canada Table 14-10-0417-01: employee wages by occupation: `data/derived/national/harvest_basis/bc_open_cost_model_strict/strict_statcan_observations.csv` (Statistics Canada Open Licence); `https://doi.org/10.25318/1410041701-eng`
- Statistics Canada Table 14-10-0064-01: employee wages by industry: `data/derived/national/harvest_basis/bc_open_cost_model_strict/strict_statcan_observations.csv` (Statistics Canada Open Licence); `https://doi.org/10.25318/1410006401-eng`
- Statistics Canada Table 18-10-0004-01: consumer price index: `data/derived/national/harvest_basis/bc_open_cost_model_strict/strict_statcan_observations.csv` (Statistics Canada Open Licence); `https://doi.org/10.25318/1810000401-eng`
- Statistics Canada Table 18-10-0281-01: for-hire motor carrier freight services price index: `data/derived/national/harvest_basis/bc_open_cost_model_strict/strict_statcan_observations.csv` (Statistics Canada Open Licence); `https://doi.org/10.25318/1810028101-eng`
- Statistics Canada Table 18-10-0283-01: machinery and equipment price index by commodity: `data/derived/national/harvest_basis/bc_open_cost_model_strict/strict_parameters.csv` (Statistics Canada Open Licence); `https://doi.org/10.25318/1810028301-eng`
- Strict-open BC logging and truck-haul cost model parameters: `data/derived/national/harvest_basis/bc_open_cost_model_strict/strict_parameters.csv` (Project-derived; CC0 assumptions + Statistics Canada Open Licence observations); `https://github.com/UBC-FRESH/clews-c2070-fresh-data`
- National facility residue supply v7 summary: `data/derived/national/facilities/facility_residue_supply_v7/summary.json` (Project-derived; see source metadata); `https://github.com/UBC-FRESH/clews-c2070-fresh-data`
- Canadian Council of Motor Transport Administrators interprovincial weights and dimensions envelope: (Public regulatory reference; not an open-data licence); `https://ccmta.ca/en/trucking/weights-and-dimensions`
- Parameter derived inside transport cost v1: (CC0 1.0 Universal public-domain dedication); ``
- Explicit engineering assumptions of transport cost v1: (CC0 1.0 Universal public-domain dedication); ``
- National facility assignment v6: `data/derived/national/facilities/national_facility_assignment_v6/facility_assignment.csv` (Project-derived; see source metadata); `https://github.com/UBC-FRESH/clews-c2070-fresh`
- Facility road-distance audit v1 province summary: `data/derived/national/facilities/facility_road_distance_audit_v1/province_road_distance_summary.csv` (Project-derived; OSRM/OpenStreetMap ODbL-1.0 routing); `https://github.com/UBC-FRESH/clews-c2070-fresh-data`
- National rest-of-Canada biomass supply curve (adopted OSeCAN tier definitions): `data/derived/national/clews/osecan/national_supply_curve/supply_curve_definition.json` (Project-derived; see source metadata); `https://github.com/UBC-FRESH/clews-c2070-fresh-data`

Reproduce: `.venv/bin/python -m workflows.national.facilities.transport_cost_v1`
