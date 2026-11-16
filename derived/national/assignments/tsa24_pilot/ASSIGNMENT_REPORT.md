# TSA24/BC Stage A Facility Assignment Pilot

> **Diagnostic pilot.** The supply area is `1,000 ha`, a
> contract/data-shape test, not a TSA24 supply estimate. Assortment sorts are
> dimension-only; no BC official grade equivalence is claimed. MKRF is not used.

## 1. Scope and Stage A/B split

Stage A consumes the TSA24 assortment matrix, parsed FFCM BC facility lines, a
diagnostic road transport layer, and diagnostic contracts, then solves a
profit-maximising transportation/allocation LP. It emits facility assignment,
utilization, contract, unassigned-supply, objective, and validation tables.
Stage B (`fresh_fibre.graph` / `fresh_fibre.lp`) consumes the Stage B
`supply_offer`, `technology`, and `transport_link` subset written alongside this
report; Stage A does not invent Stage B demand or market rows.

- Scenario: `tsa24_bc_stage_a_pilot`
- Period: `2026`
- Supply offers: 53
- Facilities: 161 screened; 130 with a transport link
- Transport links: 211
- Contracts: 161
- Total supply: 311,600 m3 green
- Solver: PULP_CBC_CMD 2.9.0 (Optimal)

## 2. Fixture

### 2.1 Supply grades

The matrix is a per-hectare TSA24 stand composition. Each detail row is scaled
by the diagnostic area; the total row is a check, not a supply offer. Residue
uses the ledger's 0.45 ODT/m3 density and 0.45 wet-basis moisture.

| Grade | Product | Offers | Supply m3 | Supply ODT | Assigned m3 | Unassigned m3 | Assigned share | Roadside CAD/m3 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| HOGFUEL | hogfuel | 0 | 0 | 0 | 0 | 0 | 0.0% | 0.00-0.00 |
| OTHER_LOG | other | 8 | 21,074 | 8,102 | 21,074 | 0 | 100.0% | 61.74-61.74 |
| PULP | pulpwood | 2 | 599 | 219 | 599 | 0 | 100.0% | 52.99-52.99 |
| RESIDUE | residue | 7 | 70,864 | 31,889 | 70,864 | 0 | 100.0% | 0.00-0.00 |
| SAWLOG | sawlog | 36 | 219,062 | 79,832 | 219,063 | 0 | 100.0% | 105.98-128.19 |

### 2.2 Facilities

Only BC `SAW`, `PAP`, `PEL`, and `BIO` facilities are in scope. Capacity is
normalized to m3/y from `m3/y` directly and from `odt/y` at 1/0.45 m3 per ODT.
`bdmt/y` capacity lines are rejected; for PAP they duplicate the paired `m3/y`
log line. Facility nameplate is the sum of the maximum normalized capacity per
primary product, so alternative feedstock lines are not counted repeatedly.

| Class | Facilities | With link | Nameplate m3/y | Assigned m3 | Utilization | Binding | Links |
| --- | --- | --- | --- | --- | --- | --- | --- |
| BIO | 12 | 11 | 8,326,259 | 0 | 0.0% | 0 | 44 |
| PAP | 15 | 11 | 30,774,260 | 21,673 | 0.1% | 0 | 33 |
| PEL | 13 | 13 | 6,859,300 | 70,864 | 1.0% | 0 | 39 |
| SAW | 121 | 95 | 45,178,430 | 219,063 | 0.5% | 0 | 95 |

Rejected processing lines (first 15):

| Facility | Line | Reason |
| --- | --- | --- |
| BC-PAP-179 | BC-PAP-179-1 | rejected_capacity_unit:capacity unit 'bdmt/y' is rejected; supported units are ['m3/y', 'odt/y'] |
| BC-PAP-589 | BC-PAP-589-1 | rejected_capacity_unit:capacity unit 'bdmt/y' is rejected; supported units are ['m3/y', 'odt/y'] |
| BC-PAP-589 | BC-PAP-589-3 | rejected_capacity_unit:capacity unit 'bdmt/y' is rejected; supported units are ['m3/y', 'odt/y'] |
| BC-PAP-511 | BC-PAP-511-1 | rejected_capacity_unit:capacity unit 'bdmt/y' is rejected; supported units are ['m3/y', 'odt/y'] |
| BC-PAP-679 | BC-PAP-679-1 | rejected_capacity_unit:capacity unit 'bdmt/y' is rejected; supported units are ['m3/y', 'odt/y'] |
| BC-PAP-731 | BC-PAP-731-1 | rejected_capacity_unit:capacity unit 'bdmt/y' is rejected; supported units are ['m3/y', 'odt/y'] |
| BC-PAP-590 | BC-PAP-590-1 | rejected_capacity_unit:capacity unit 'bdmt/y' is rejected; supported units are ['m3/y', 'odt/y'] |
| BC-PAP-938 | BC-PAP-938-1 | rejected_capacity_unit:capacity unit 'bdmt/y' is rejected; supported units are ['m3/y', 'odt/y'] |
| BC-PAP-591 | BC-PAP-591-1 | rejected_capacity_unit:capacity unit 'bdmt/y' is rejected; supported units are ['m3/y', 'odt/y'] |
| BC-PAP-957 | BC-PAP-957-1 | rejected_capacity_unit:capacity unit 'bdmt/y' is rejected; supported units are ['m3/y', 'odt/y'] |
| BC-PAP-963 | BC-PAP-963-1 | rejected_capacity_unit:capacity unit 'bdmt/y' is rejected; supported units are ['m3/y', 'odt/y'] |
| BC-PAP-964 | BC-PAP-964-1 | rejected_capacity_unit:capacity unit 'bdmt/y' is rejected; supported units are ['m3/y', 'odt/y'] |
| BC-PAP-1007 | BC-PAP-1007-1 | rejected_capacity_unit:capacity unit 'bdmt/y' is rejected; supported units are ['m3/y', 'odt/y'] |
| BC-PAP-1008 | BC-PAP-1008-1 | rejected_capacity_unit:capacity unit 'bdmt/y' is rejected; supported units are ['m3/y', 'odt/y'] |
| BC-PAP-1163 | BC-PAP-1163-1 | rejected_capacity_unit:capacity unit 'bdmt/y' is rejected; supported units are ['m3/y', 'odt/y'] |

Facilities without an FFCM road route to a transload node are excluded from the
transport layer, not given a fabricated distance. Rejected facilities:
31.

### 2.3 Transport

The archive has no TSA24 supply-node-to-transload route. The pilot therefore
uses the minimum FFCM facility-to-`TL` road distance plus a documented
`150 km` TSA24 access leg. This is a diagnostic road
estimate, not a Euclidean distance and not a production route. The facility leg
is from `routes.csv`; the supply leg is an assumption. Road cost uses
`BC_logging_truck` for logs and `BC_residue_truck` for residue, with archive
fuel/operating rates and truck capacities. No transload cost is applied because
the diagnostic path is direct road. Route capacity is absent from the parsed
route table, so links are uncapped.

### 2.4 Contracts

No populated contract table exists in the archive. Each facility receives a
diagnostic contract with `min=0`, `max=nameplate`, and `gate=0`. Contract
compliance is therefore a bound check, not evidence about real commercial terms.

## 3. LP formulation

Maximise product revenue minus roadside supply, transport, gate, processing,
and unassigned penalty:

```
max  sum_{s,f,g,t} (R_fg - C_s - H_sf - G_fg - P_fg) x[s,f,g,t]
     - penalty * sum_{s,g,t} u[s,g,t]
```

Subject to:

- supply balance: `sum_f x[s,f,g,t] + u[s,g,t] = V_s`
- facility nameplate: `sum_{s,g} x[s,f,g,t] <= nameplate_f`
- grade capacity: `sum_s x[s,f,g,t] <= capacity_fg`
- contract minimum/maximum per facility and period
- optional moisture blend: `sum_s M_s x <= limit_f * sum_s x`
- optional transport-link capacity
- `x >= 0`, `u >= 0`; no binaries in this pilot

There are no `y[f,l,t]` line-activity variables because the fixture aggregates
alternative feedstock lines into one grade-specific capacity and keeps the
facility nameplate as the total cap. `x` is in m3 green; `u` is in the same
basis. The multi-period key is present, but the pilot uses one period.

## 4. Results

### 4.1 Assigned versus unassigned by grade

| Grade | Product | Offers | Supply m3 | Supply ODT | Assigned m3 | Unassigned m3 | Assigned share | Roadside CAD/m3 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| HOGFUEL | hogfuel | 0 | 0 | 0 | 0 | 0 | 0.0% | 0.00-0.00 |
| OTHER_LOG | other | 8 | 21,074 | 8,102 | 21,074 | 0 | 100.0% | 61.74-61.74 |
| PULP | pulpwood | 2 | 599 | 219 | 599 | 0 | 100.0% | 52.99-52.99 |
| RESIDUE | residue | 7 | 70,864 | 31,889 | 70,864 | 0 | 100.0% | 0.00-0.00 |
| SAWLOG | sawlog | 36 | 219,062 | 79,832 | 219,063 | 0 | 100.0% | 105.98-128.19 |

### 4.2 Facility utilization by class

| Class | Facilities | With link | Nameplate m3/y | Assigned m3 | Utilization | Binding | Links |
| --- | --- | --- | --- | --- | --- | --- | --- |
| BIO | 12 | 11 | 8,326,259 | 0 | 0.0% | 0 | 44 |
| PAP | 15 | 11 | 30,774,260 | 21,673 | 0.1% | 0 | 33 |
| PEL | 13 | 13 | 6,859,300 | 70,864 | 1.0% | 0 | 39 |
| SAW | 121 | 95 | 45,178,430 | 219,063 | 0.5% | 0 | 95 |

### 4.3 Capacity binding

No facility reached nameplate capacity in this run.

### 4.4 Largest assignments

| Facility | Class | Assigned m3 | Nameplate m3/y | Utilization |
| --- | --- | --- | --- | --- |
| BC-SAW-981 | SAW | 219,063 | 394,122 | 55.6% |
| BC-PEL-1650 | PEL | 70,864 | 1,004,500 | 7.1% |
| BC-PAP-964 | PAP | 21,673 | 1,730,006 | 1.3% |

### 4.5 Contract compliance

161 of 161 diagnostic contracts satisfy both bounds.
All contracts are marked `diagnostic`.

### 4.6 Objective decomposition

| Component | Value CAD | Unit | Notes |
| --- | --- | --- | --- |
| product_revenue | 44,018,710.11 | CAD | assigned volume x facility product revenue |
| supply_cost | -26,275,684.72 | CAD | assigned volume x roadside cost proxy |
| transport_cost | -2,589,728.73 | CAD | assigned volume x diagnostic road cost |
| gate_cost | -0.00 | CAD | assigned volume x contract gate cost |
| processing_cost | -12,581,427.77 | CAD | assigned volume x line processing cost |
| unassigned_penalty | 0.00 | CAD | unassigned volume x diagnostic penalty |
| net_objective | 2,571,868.89 | CAD | solver objective 2571868.886798 |

### 4.7 Facility-class mix versus FFCM

| Class | Pilot assigned m3 | Pilot share | FFCM fmu-primary share |
| --- | --- | --- | --- |
| SAW | 219,063 | 70.3% | 85.8% |
| PAP | 21,673 | 7.0% | 4.1% |
| PEL | 70,864 | 22.7% | 7.0% |
| BIO | 0 | 0.0% | 3.0% |

FFCM shares are primary `fmu -> facility` variable families from `lp-variable-families.csv`; PLY/OSB/export and secondary processor-to-processor families are outside this pilot and are excluded from both shares. The comparison is directional, not a calibration target.

## 5. Validation

| Check | Pass | Detail |
| --- | --- | --- |
| solver_status | yes | status=Optimal |
| volume_conservation | yes | assigned + unassigned equals supply for every offer |
| supply_reference_integrity | yes | all assignment rows reference a declared supply offer |
| grade_eligibility | yes | every assignment has a declared eligible grade and transport link |
| capacity | yes | no assignment exceeds a facility or grade capacity |
| facility_nameplate | yes | aggregate facility assignments stay within nameplate |
| contract_bounds | yes | all contracts satisfy min/max bounds |
| unassigned_reasons | yes | every unassigned row has a documented reason |
| moisture_blend | yes | facility moisture blends respect declared limits |
| unit_consistency | yes | all quantities use m3 and every capacity conversion is documented |
| finite_values | yes | all assignment and slack values are finite |
| objective_reconciliation | yes | objective decomposition reconciles to the solver objective |
| utilization_reconciliation | yes | facility utilization rows reconcile to assignments |
| contract_report_completeness | yes | every contract has a compliance row |

Overall validation: **PASS**.

## 6. Assumptions and unit conversions

| Category | Assumption | Value | Unit | Evidence |
| --- | --- | --- | --- | --- |
| scope | TSA24/BC Stage A pilot supply area is a diagnostic scale, not a TSA supply estimate. | 1000.0 | ha | diagnostic |
| supply | Assortment matrix rows are per-hectare values; the pilot multiplies by the diagnostic area. | 311.6 | m3/ha | derived_tsa24_assortment_matrix |
| supply | Roadside cost is the assortment matrix price_cad_m3 proxy, not a harvest/stumpage cost. |  | CAD/m3 | derived_tsa24_assortment_matrix |
| residue | Residue volume uses the ledger 0.45 ODT/m3 basic density and 0.45 wet-basis moisture. | 0.45 | ODT/m3 | tsa24_residue_ledger_assumption |
| facility_capacity | m3/y infeed is used directly; odt/y infeed is converted at 1/0.45 m3 per ODT; bdmt/y is rejected. | 2.2222222222222223 | m3/ODT | archive_parsed_processing_lines;ledger_density |
| facility_capacity | Facility nameplate is the sum of the maximum normalized capacity per primary product; feedstock alternatives are not additive. |  | m3/y | archive_parsed_processing_lines |
| transport | The TSA24 supply node has no archive route to an FFCM transload hub; a 150 km access leg is added to the minimum facility-to-TL road distance. | 150.0 | km | diagnostic |
| transport | Road cost uses BC_logging_truck for logs and BC_residue_truck for residue, with archive fuel and operating rates. | 0.056196031959508314 | CAD/m3-km | archive_parsed_transporters;transporter_materials |
| transport | FFCM route capacity is absent from the parsed route table; pilot transport links are uncapped. |  | m3 | diagnostic |
| contracts | Contracts are diagnostic: min=0 and max=facility nameplate. |  | m3 | diagnostic_no_populated_contract_table |
| objective | Unassigned supply carries a diagnostic penalty so that feasible supply is not silently dropped. | 1000.0 | CAD/m3 | diagnostic |
| grade | Assortment sorts are dimension-only; no BC official grade equivalence is claimed. |  | grade | derived_tsa24_assortment_matrix |
| scope | MKRF is not used anywhere in this pilot. |  | n/a | scope_rule |

The full assumption list, including rejected lines and rejected transport
links, is written to `assumptions.csv`, `line_screen.csv`, and
`transport_screen.csv`.

## 7. Gaps and next steps

- Replace the diagnostic 150 km TSA24 access leg with a real TSA24 supply-node
  to transload/facility route or an accepted haul-distance model.
- Replace the diagnostic contracts with populated minimum/maximum terms.
- Add route/transload capacity and water/rail alternatives; the current pilot
  is road-only and uncapped.
- Normalize `bdmt/y`/`admt/y` capacity only after an accepted project
  convention; the pilot rejects bdmt capacity rather than guessing.
- Add mill-residue supply (sawdust/woodchips/hogfuel) if the Stage A scope is
  extended beyond logging residue.
- Add multi-period inventory, demand/market clearing, and line-level `y`
  variables only when the data support them.
- Do not interpret the 1,000 ha result as a TSA24 supply estimate. The optional
  ws4-quota sensitivity is a period-scale diagnostic and must be labeled as
  such.
