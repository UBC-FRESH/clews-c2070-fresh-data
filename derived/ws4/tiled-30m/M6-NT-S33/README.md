# WS4 tiled 30-m dataset — M6|NT|S33

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `M6|NT|S33` (parent `M6|NT`)
- Tile / row / col: `M6` / 3 / 3
- Province: `NT`
- Centroid: 60.055415, -123.147921
- Allocated harvest: 80.699135 m3
- Productive subcell area: 34483.899127 ha
- Committed geometry area: 41213.999513 ha
- Clipped inventory geometry: 41213.999513 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 438438
- Blocks: 186822
- Forest area: 39459.42 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 18503
- Scheduled area: 3827.07 ha
- Eligible blocks (age class >= 40): 185025
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 6.50 MB
- Schedules: 0.21 MB
- Runs: 0.00 MB
- Total: 6.71 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
