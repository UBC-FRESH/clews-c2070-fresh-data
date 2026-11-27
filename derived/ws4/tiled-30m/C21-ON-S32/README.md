# WS4 tiled 30-m dataset — C21|ON|S32

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `C21|ON|S32` (parent `C21|ON`)
- Tile / row / col: `C21` / 3 / 2
- Province: `ON`
- Centroid: 48.720588, -85.267746
- Allocated harvest: 64363.313747 m3
- Productive subcell area: 224804.520499 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2444853
- Blocks: 905236
- Forest area: 220036.77 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 77656
- Scheduled area: 15755.58 ha
- Eligible blocks (age class >= 40): 776552
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 30.18 MB
- Schedules: 0.92 MB
- Runs: 0.00 MB
- Total: 31.10 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
