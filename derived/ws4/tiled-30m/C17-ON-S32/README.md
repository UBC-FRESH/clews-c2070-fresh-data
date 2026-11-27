# WS4 tiled 30-m dataset — C17|ON|S32

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `C17|ON|S32` (parent `C17|ON`)
- Tile / row / col: `C17` / 3 / 2
- Province: `ON`
- Centroid: 49.200082, -93.433154
- Allocated harvest: 42528.381478 m3
- Productive subcell area: 192750.045359 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2010425
- Blocks: 812139
- Forest area: 180938.25 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 72563
- Scheduled area: 13387.95 ha
- Eligible blocks (age class >= 40): 725624
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 25.48 MB
- Schedules: 0.86 MB
- Runs: 0.00 MB
- Total: 26.34 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
