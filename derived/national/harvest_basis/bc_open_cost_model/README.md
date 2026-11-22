# BC open-data logging and truck-haul cost model

**Status:** proxy model built only from public data. This is **not** an observed
contractor cost, a mill settlement, or a net-value estimate.

## What is modelled

- **Tree-to-truck logging:** all-found 2026 BC machine rates divided by public
  FPInnovations/FERIC scheduled-hour productivity, by rate group and system.
  Ground extraction uses a coastal loader-forwarder for Coast appraisal rows and
  a grapple skidder for Interior appraisal rows.
- **Truck haul:** IAM 2026 cycle-time/haul equation combined with an all-found
  truck-cycle model for Interior appraisal rows; the all-found truck-cycle model
  alone for Coast appraisal rows (the CAM publishes no general truck-haul
  equation). The appraisal region, not the rate group, selects the method.
- **Sensitivity:** slope, piece size, sale volume and haul distance.

The model deliberately does **not** use ILCR/CCTMCS microdata, FPInterface,
confidential mill settlements, or any restricted input.

## Formulas

Logging, per phase:

```
phase_cost_CAD_m3 = all_found_rate_CAD_SMH / productivity_m3_SMH
```

System cost is the sum of felling, extraction, processing and loading phases.
The low/high range uses the lowest/highest published machine class and a
+20%/-25% productivity band.

Adjustments (labelled proxy because the coefficients come from the IAM
estimated-winning-bid equation, not from a cost survey):

```
slope_add  = 0.2204 * max(0, slope_pct - 15) * system_factor
piece_add  = -9.321 * ln(piece_size_m3 / 0.60) * system_factor
volume_add = clamp(-4.306 * ln(sale_volume_m3 / 20000), -6, +6) * system_factor
```

`system_factor` is 1.0 for ground, 0.5 for cable, and 0.0/0.5 for helicopter
(slope/piece/volume respectively).

Truck haul, Interior published equation:

```
haul_CAD_m3 = 2.407 * CPIF * CYCLE_hours
CYCLE = 1 km at 10 km/h loaded + 1 km at 15 km/h empty
        + road distance at 55 km/h loaded + 65 km/h empty
        + 78 min unavoidable delay + 0.5 h loading/unloading
```

Truck haul, engineering cross-check:

```
haul_CAD_m3 = (truck_tractor_CAD_SMH + trailer_CAD_SMH) * CYCLE_hours / payload_m3
```

For the Interior the base is the geometric mean of the published equation and
the engineering model; for the Coast the engineering model is used because the
CAM publishes no general truck-haul equation. North West Zone is appraisal-
Interior and therefore uses the Interior method, while its machine rates come
from the coastal/northwest rate group. The low/high bounds use the published
low/high truck and trailer rates and the IAM CPIF range of 0.95-1.05.

## Coverage

- 7 BC forest zones with explicit appraisal regions: 1 Coast and 6 Interior.
- Two TLA hourly-rate groups: coastal/northwest and southern/northern Interior.
- 5 slope scenarios (10, 28, 42, 55, 70%) mapped to ground, cable and
  helicopter systems.
- 3 piece sizes (0.30, 0.60, 1.00 m3/tree).
- 3 sale volumes (5,000, 20,000, 100,000 m3).
- 3 truck-haul distances (50, 100, 150 km).
- 945 estimate rows in total.

## Published vs proxy

| Element | Status |
|---|---|
| All-found machine rates | Published 2026 rate guide |
| Phase productivity | Published case studies, used as scheduled-hour proxy |
| IAM haul equation | Published appraisal rule |
| Slope/piece/volume coefficients | Published IAM coefficients, used as cost proxies |
| Helicopter allowance | Published IAM specified-operation allowance, used as total proxy |
| Payload 45-60 m3 | Published weight limits + density conversion, proxy |
| Road speeds 55/65 km/h | Proxy; district schedules are not public |
| Regional zone mapping | Proxy; rate guide publishes two groups, with an explicit appraisal-region crosswalk |

## Worked example

FPInnovations ADV5N19, coastal swing yarder:

- published machine rate: 335.51 CAD/SMH
- scheduled hours: 117 h; volume: 3,640 m3; productivity: 31.11 m3/SMH
- cost = 335.51 / 31.11 = **10.79 CAD/m3**; the report prints **10.78 CAD/m3**
  (rounding of the reported productivity).

IAM 2026 haul example at a 3.0 h cycle and CPIF = 1.0:

```
2.407 * 3.0 * 1.0 = 7.22 CAD/m3
```

## Files

| File | Rows | Purpose |
|---|---:|---|
| `bc_open_cost_parameters.csv` | 38 | Formula, coefficient, unit, applicability, source and licence |
| `bc_open_cost_estimates.csv` | 945 | Zone x scenario logging/haul/total low-base-high |
| `bc_open_cost_sensitivity.csv` | 10 | One-at-a-time sensitivity cases |
| `bc_open_cost_sources.csv` | 10 | Public source register and hashes |
| `manifest.json` | - | Inputs, outputs, validation and spot checks |

## Source register

| Source key | Title | Year | Licence |
|---|---|---:|---|
| `tla_rate_guide_2026_08` | BC Timber Harvest Cost Model Rate Guide, August 2026 | 2026 | Public PDF; TLA/ILA/NWLA/MNP copyright. Not redistributed. |
| `fpinnovations_adv2n54` | Roadside harvesting with low ground-pressure skidders in northwestern British Columbia | 2001 | Public FPInnovations Advantage report; publisher copyright. |
| `fpinnovations_adv5n19` | Implementing new forest management principles in coastal British Columbia: case study 1 | 2004 | Public FPInnovations Advantage report; publisher copyright. |
| `fpinnovations_adv3n19` | Helicopter logging in British Columbia: clearcut harvesting with the Sikorsky S-64E and S-64F Skycrane helicopters | 2002 | Public FPInnovations Advantage report; publisher copyright. |
| `fpinnovations_adv11n27` | Cost and productivity of alternative harvesting in interior British Columbia wet belt to maintain caribou habitat | 2010 | Public FPInnovations Advantage report; publisher copyright. |
| `bc_iam_2026` | Interior Appraisal Manual, effective 2026-07-01 | 2026 | BC Crown copyright; public PDF. |
| `bc_cam_2026` | Coast Appraisal Manual, effective 2026-01-01 | 2026 | BC Crown copyright; public PDF. |
| `bc_cvse_logging_truck_configurations` | Approved logging truck configurations (Commercial Transport Regulations s.7.26) | 2025 | BC Crown copyright; public PDF. |
| `fpinnovations_9axle_2021` | 9-axle B-trains for log hauling on BC resource roads | 2021 | Public report; publisher copyright. |
| `bc_bcts_results` | BC Timber Sales public timber sale results | 2026 | BC Crown copyright; public web results. |

Full URLs, SHA-256 hashes, retrieval timestamps and the exact table/section
used are in `bc_open_cost_sources.csv` and `manifest.json`.

## Source search log

| Source | What was checked | Finding |
|---|---|---|
| IAM 2026 | Sections 3.2.12 (cycle time), 3.3.4 (specified operations), 3.4 (transportation route), 4.3 (road/silviculture) | No general tree-to-truck $/m3 table. Logging is embedded in the EWB. A published haul equation (`2.407 x CYCLE x CPIF`) and slope/piece/volume coefficients exist. |
| CAM 2026 | Sections 4.3-4.4 (EWB, specified operations), 5.3 (road), 5.7 (silviculture) | No general logging or truck-haul $/m3 table. Long-haul is a marginal $0.171/m3/km beyond 100 km; barge/tow are route-specific. |
| BCTS public sale results | 2026 awarded/unsold sale pages | Pages expose volume, upset, bonus and bidder count only. They do not expose appraisal logging, haul, road or stumpage components. |
| BC MPS updates 2025 | Interior/Coast specified operations and tenure adjustments | Confirms logging and haul are embedded in the MPS/EWB; only special systems (skyline, helicopter, horse, rail, barge) have published $/m3 allowances. |
| TLA/ILA/NWLA 2026 rate guide | All-found machine rates, region groups, assumptions | Supplies current hourly rates; no productivity or $/m3 cost. Productivity must come from case studies. |
| FPInnovations/FERIC case studies | ADV2N54, ADV5N19, ADV3N19, ADV11N27 | Supply phase productivity, utilisation and case-study $/m3. Used as the productivity layer, not as a BC-wide survey. |
| BC CVSE / Commercial Transport Regulations | Logging truck configurations and s.7.26 | Supplies the 63,500 kg GCVW cap and axle limits used to bound payload. |
| FPInnovations 9-axle B-train report | Payload table by configuration | Supplies the 43-50 t payload range and the 50 m3 central payload proxy. |

## Validation

- 945 estimate rows, no NaN, infinite or negative values.
- Every row satisfies `total_low <= total_base <= total_high`.
- All 7 forest zones and all 3 systems (ground, cable, helicopter) are present.
- Every parameter row has a formula, coefficient, unit, applicability, source
  and licence.
- `manifest.json` records SHA-256 hashes for every input used and every output
  written.
- The model fails closed on missing source PDFs, hash mismatches, unknown
  systems, zero/negative rates or productivities, and unordered cost ranges.

## How this feeds an open-data net-value estimate

The model supplies the two missing BC cost components that previously forced
`net_value_status=not_estimated`: tree-to-truck logging and general truck haul.
A net-value calculation can now subtract a **range** from a public
mill-delivered log price or a standing-timber stumpage benchmark, while keeping
the result labelled `net_value_status=model_estimate` and
`cost_basis=open_proxy_model`. It must still add road, bridge,
culvert, silviculture and tenure allowances separately, and it must not label
the residual as an observed profit or an official net value.
