# WS4 tiled 30-m dataset — E32|NS|S23

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `E32|NS|S23` (parent `E32|NS`)
- Tile / row / col: `E32` / 2 / 3
- Province: `NS`
- Centroid: 45.715400, -62.955806
- Allocated harvest: 18287.343627 m3
- Productive subcell area: 39001.358114 ha
- Committed geometry area: 48202.479199 ha
- Clipped inventory geometry: 48202.479199 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 376687
- Blocks: 140366
- Forest area: 33901.83 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 9881
- Scheduled area: 1842.12 ha
- Eligible blocks (age class >= 40): 98805
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 5.40 MB
- Schedules: 0.11 MB
- Runs: 0.00 MB
- Total: 5.52 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
