# WS4 tiled 30-m dataset — C23|ON|S33

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `C23|ON|S33` (parent `C23|ON`)
- Tile / row / col: `C23` / 3 / 3
- Province: `ON`
- Centroid: 48.128825, -80.632819
- Allocated harvest: 60746.402306 m3
- Productive subcell area: 219318.652196 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2495004
- Blocks: 887521
- Forest area: 224550.36 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 79252
- Scheduled area: 17376.39 ha
- Eligible blocks (age class >= 40): 792516
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 30.74 MB
- Schedules: 0.94 MB
- Runs: 0.00 MB
- Total: 31.68 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
