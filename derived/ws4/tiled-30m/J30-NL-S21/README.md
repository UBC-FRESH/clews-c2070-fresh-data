# WS4 tiled 30-m dataset — J30|NL|S21

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `J30|NL|S21` (parent `J30|NL`)
- Tile / row / col: `J30` / 2 / 1
- Province: `NL`
- Centroid: 53.552146, -62.783859
- Allocated harvest: 11545.989849 m3
- Productive subcell area: 185193.892643 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1904462
- Blocks: 763978
- Forest area: 171401.58 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 67939
- Scheduled area: 15479.73 ha
- Eligible blocks (age class >= 40): 679382
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 24.21 MB
- Schedules: 0.81 MB
- Runs: 0.00 MB
- Total: 25.02 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
