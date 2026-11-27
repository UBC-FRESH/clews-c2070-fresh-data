# WS4 tiled 30-m dataset — L11|AB|S21

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `L11|AB|S21` (parent `L11|AB`)
- Tile / row / col: `L11` / 2 / 1
- Province: `AB`
- Centroid: 59.955608, -110.660671
- Allocated harvest: 6942.823333 m3
- Productive subcell area: 32879.048310 ha
- Committed geometry area: 42572.238379 ha
- Clipped inventory geometry: 42572.238379 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 371392
- Blocks: 81839
- Forest area: 33425.28 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 6411
- Scheduled area: 1564.56 ha
- Eligible blocks (age class >= 40): 64109
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 4.07 MB
- Schedules: 0.07 MB
- Runs: 0.00 MB
- Total: 4.14 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
