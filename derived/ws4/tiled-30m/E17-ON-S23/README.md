# WS4 tiled 30-m dataset — E17|ON|S23

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `E17|ON|S23` (parent `E17|ON`)
- Tile / row / col: `E17` / 2 / 3
- Province: `ON`
- Centroid: 51.443493, -92.618501
- Allocated harvest: 40949.682342 m3
- Productive subcell area: 193617.098470 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2200515
- Blocks: 813262
- Forest area: 198046.35 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 77206
- Scheduled area: 16970.58 ha
- Eligible blocks (age class >= 40): 772051
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 27.12 MB
- Schedules: 0.92 MB
- Runs: 0.00 MB
- Total: 28.04 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
