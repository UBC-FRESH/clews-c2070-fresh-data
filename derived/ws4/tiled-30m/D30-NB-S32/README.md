# WS4 tiled 30-m dataset — D30|NB|S32

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `D30|NB|S32` (parent `D30|NB`)
- Tile / row / col: `D30` / 3 / 2
- Province: `NB`
- Centroid: 46.508498, -67.505039
- Allocated harvest: 188767.666223 m3
- Productive subcell area: 195591.415647 ha
- Committed geometry area: 223535.672974 ha
- Clipped inventory geometry: 223535.672974 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1981778
- Blocks: 697373
- Forest area: 178360.02 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 58414
- Scheduled area: 12245.85 ha
- Eligible blocks (age class >= 40): 584138
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 23.70 MB
- Schedules: 0.69 MB
- Runs: 0.00 MB
- Total: 24.39 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
