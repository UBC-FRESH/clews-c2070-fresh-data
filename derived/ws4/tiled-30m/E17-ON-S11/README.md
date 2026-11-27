# WS4 tiled 30-m dataset — E17|ON|S11

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `E17|ON|S11` (parent `E17|ON`)
- Tile / row / col: `E17` / 1 / 1
- Province: `ON`
- Centroid: 51.014062, -94.079974
- Allocated harvest: 40949.682342 m3
- Productive subcell area: 193617.098470 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2018990
- Blocks: 637497
- Forest area: 181709.10 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 51769
- Scheduled area: 14466.69 ha
- Eligible blocks (age class >= 40): 517685
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 22.96 MB
- Schedules: 0.61 MB
- Runs: 0.00 MB
- Total: 23.57 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
