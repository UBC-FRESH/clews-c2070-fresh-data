# WS4 tiled 30-m dataset — B26|ON|S22

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `B26|ON|S22` (parent `B26|ON`)
- Tile / row / col: `B26` / 2 / 2
- Province: `ON`
- Centroid: 45.383568, -76.297883
- Allocated harvest: 31145.669591 m3
- Productive subcell area: 103073.612330 ha
- Committed geometry area: 129656.460630 ha
- Clipped inventory geometry: 129656.460630 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 737661
- Blocks: 293731
- Forest area: 66389.49 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 24330
- Scheduled area: 5518.17 ha
- Eligible blocks (age class >= 40): 243294
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 9.91 MB
- Schedules: 0.28 MB
- Runs: 0.00 MB
- Total: 10.20 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
