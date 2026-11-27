# WS4 tiled 30-m dataset — J9|AB|S11

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `J9|AB|S11` (parent `J9|AB`)
- Tile / row / col: `J9` / 1 / 1
- Province: `AB`
- Centroid: 56.297873, -114.040668
- Allocated harvest: 105766.628084 m3
- Productive subcell area: 224033.462209 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2457676
- Blocks: 784810
- Forest area: 221190.84 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 66701
- Scheduled area: 17542.08 ha
- Eligible blocks (age class >= 40): 667008
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 28.65 MB
- Schedules: 0.79 MB
- Runs: 0.00 MB
- Total: 29.44 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
