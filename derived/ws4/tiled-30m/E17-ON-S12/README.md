# WS4 tiled 30-m dataset — E17|ON|S12

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `E17|ON|S12` (parent `E17|ON`)
- Tile / row / col: `E17` / 1 / 2
- Province: `ON`
- Centroid: 51.004960, -93.362455
- Allocated harvest: 40949.682342 m3
- Productive subcell area: 193617.098470 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2080342
- Blocks: 712228
- Forest area: 187230.78 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 63318
- Scheduled area: 13885.92 ha
- Eligible blocks (age class >= 40): 633175
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 24.46 MB
- Schedules: 0.75 MB
- Runs: 0.00 MB
- Total: 25.21 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
