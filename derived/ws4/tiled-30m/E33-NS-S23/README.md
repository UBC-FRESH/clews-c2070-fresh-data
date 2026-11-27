# WS4 tiled 30-m dataset — E33|NS|S23

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `E33|NS|S23` (parent `E33|NS`)
- Tile / row / col: `E33` / 2 / 3
- Province: `NS`
- Centroid: 45.300912, -61.390058
- Allocated harvest: 44099.649159 m3
- Productive subcell area: 91754.842228 ha
- Committed geometry area: 110675.185948 ha
- Clipped inventory geometry: 110675.185948 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 993004
- Blocks: 421830
- Forest area: 89370.36 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 35544
- Scheduled area: 6710.67 ha
- Eligible blocks (age class >= 40): 355439
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 13.02 MB
- Schedules: 0.42 MB
- Runs: 0.00 MB
- Total: 13.44 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
