# WS4 tiled 30-m dataset — C21|ON|S22

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `C21|ON|S22` (parent `C21|ON`)
- Tile / row / col: `C21` / 2 / 2
- Province: `ON`
- Centroid: 48.277022, -85.370122
- Allocated harvest: 64363.313747 m3
- Productive subcell area: 224804.520499 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2520539
- Blocks: 974311
- Forest area: 226848.51 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 91037
- Scheduled area: 19662.93 ha
- Eligible blocks (age class >= 40): 910365
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 31.85 MB
- Schedules: 1.08 MB
- Runs: 0.00 MB
- Total: 32.93 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
