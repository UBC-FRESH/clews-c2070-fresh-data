# WS4 tiled 30-m dataset — L30|NL|S13

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `L30|NL|S13` (parent `L30|NL`)
- Tile / row / col: `L30` / 1 / 3
- Province: `NL`
- Centroid: 54.998215, -59.453357
- Allocated harvest: 5531.707696 m3
- Productive subcell area: 80927.419391 ha
- Committed geometry area: 166743.676602 ha
- Clipped inventory geometry: 166743.676602 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1028596
- Blocks: 377318
- Forest area: 92573.64 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 29025
- Scheduled area: 7366.77 ha
- Eligible blocks (age class >= 40): 290246
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 12.62 MB
- Schedules: 0.34 MB
- Runs: 0.00 MB
- Total: 12.96 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
