# WS4 tiled 30-m dataset — D21|ON|S31

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `D21|ON|S31` (parent `D21|ON`)
- Tile / row / col: `D21` / 3 / 1
- Province: `ON`
- Centroid: 50.123592, -85.640640
- Allocated harvest: 43833.125097 m3
- Productive subcell area: 223173.850989 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2656977
- Blocks: 839585
- Forest area: 239127.93 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 81108
- Scheduled area: 21918.15 ha
- Eligible blocks (age class >= 40): 811076
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 31.04 MB
- Schedules: 0.96 MB
- Runs: 0.00 MB
- Total: 32.00 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
