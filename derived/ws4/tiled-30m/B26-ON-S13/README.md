# WS4 tiled 30-m dataset — B26|ON|S13

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `B26|ON|S13` (parent `B26|ON`)
- Tile / row / col: `B26` / 1 / 3
- Province: `ON`
- Centroid: 44.934559, -75.866246
- Allocated harvest: 60054.218354 m3
- Productive subcell area: 198743.687413 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1583563
- Blocks: 623346
- Forest area: 142520.67 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 50137
- Scheduled area: 11888.19 ha
- Eligible blocks (age class >= 40): 501363
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 20.39 MB
- Schedules: 0.59 MB
- Runs: 0.00 MB
- Total: 20.99 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
