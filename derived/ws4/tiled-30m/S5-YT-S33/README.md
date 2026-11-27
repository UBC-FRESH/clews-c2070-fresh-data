# WS4 tiled 30-m dataset — S5|YT|S33

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `S5|YT|S33` (parent `S5|YT`)
- Tile / row / col: `S5` / 3 / 3
- Province: `YT`
- Centroid: 66.323424, -135.250245
- Allocated harvest: 200.402540 m3
- Productive subcell area: 134571.201402 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1574669
- Blocks: 524413
- Forest area: 141720.21 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 36524
- Scheduled area: 10394.55 ha
- Eligible blocks (age class >= 40): 365237
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 18.59 MB
- Schedules: 0.43 MB
- Runs: 0.00 MB
- Total: 19.02 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
