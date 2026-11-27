# WS4 tiled 30-m dataset — H13|MB|S33

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `H13|MB|S33` (parent `H13|MB`)
- Tile / row / col: `H13` / 3 / 3
- Province: `MB`
- Centroid: 55.823069, -101.847085
- Allocated harvest: 2428.786602 m3
- Productive subcell area: 62088.460001 ha
- Committed geometry area: 84707.127747 ha
- Clipped inventory geometry: 84707.127747 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 542847
- Blocks: 123396
- Forest area: 48856.23 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 8149
- Scheduled area: 1407.51 ha
- Eligible blocks (age class >= 40): 81490
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 5.87 MB
- Schedules: 0.09 MB
- Runs: 0.00 MB
- Total: 5.96 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
