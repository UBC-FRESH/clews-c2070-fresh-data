# WS4 tiled 30-m dataset — B26|ON|S33

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `B26|ON|S33` (parent `B26|ON`)
- Tile / row / col: `B26` / 3 / 3
- Province: `ON`
- Centroid: 45.534896, -75.305124
- Allocated harvest: 896.532126 m3
- Productive subcell area: 2966.987257 ha
- Committed geometry area: 3732.177982 ha
- Clipped inventory geometry: 3732.177982 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 12979
- Blocks: 5475
- Forest area: 1168.11 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 3778
- Scheduled area: 852.12 ha
- Eligible blocks (age class >= 40): 3778
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 0.28 MB
- Schedules: 0.04 MB
- Runs: 0.00 MB
- Total: 0.32 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
