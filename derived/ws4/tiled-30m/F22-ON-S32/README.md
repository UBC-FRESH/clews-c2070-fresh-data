# WS4 tiled 30-m dataset — F22|ON|S32

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `F22|ON|S32` (parent `F22|ON`)
- Tile / row / col: `F22` / 3 / 2
- Province: `ON`
- Centroid: 52.473869, -82.061264
- Allocated harvest: 8037.559633 m3
- Productive subcell area: 121145.440609 ha
- Committed geometry area: 231146.429485 ha
- Clipped inventory geometry: 231146.429485 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1299793
- Blocks: 496508
- Forest area: 116981.37 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 43154
- Scheduled area: 10880.91 ha
- Eligible blocks (age class >= 40): 431532
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 16.74 MB
- Schedules: 0.51 MB
- Runs: 0.00 MB
- Total: 17.25 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
