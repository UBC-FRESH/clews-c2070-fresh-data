# WS4 tiled 30-m dataset — H21|ON|S13

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `H21|ON|S13` (parent `H21|ON`)
- Tile / row / col: `H21` / 1 / 3
- Province: `ON`
- Centroid: 54.452572, -82.937099
- Allocated harvest: 4130.880255 m3
- Productive subcell area: 76275.754459 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1176546
- Blocks: 425663
- Forest area: 105889.14 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 33378
- Scheduled area: 9272.52 ha
- Eligible blocks (age class >= 40): 333779
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 14.81 MB
- Schedules: 0.39 MB
- Runs: 0.00 MB
- Total: 15.21 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
