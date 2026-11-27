# WS4 tiled 30-m dataset — O12|NT|S23

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `O12|NT|S23` (parent `O12|NT`)
- Tile / row / col: `O12` / 2 / 3
- Province: `NT`
- Centroid: 64.580058, -107.781871
- Allocated harvest: 0.898322 m3
- Productive subcell area: 1925.779452 ha
- Committed geometry area: 96770.098118 ha
- Clipped inventory geometry: 96770.098118 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 27535
- Blocks: 24547
- Forest area: 2478.15 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 862
- Scheduled area: 82.44 ha
- Eligible blocks (age class >= 40): 8615
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 0.73 MB
- Schedules: 0.01 MB
- Runs: 0.00 MB
- Total: 0.74 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
