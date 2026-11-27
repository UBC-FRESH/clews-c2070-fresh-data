# WS4 tiled 30-m dataset — L9|AB|S11

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `L9|AB|S11` (parent `L9|AB`)
- Tile / row / col: `L9` / 1 / 1
- Province: `AB`
- Centroid: 58.925979, -115.618746
- Allocated harvest: 98025.289357 m3
- Productive subcell area: 196257.628929 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2462668
- Blocks: 500312
- Forest area: 221640.12 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 40275
- Scheduled area: 10556.55 ha
- Eligible blocks (age class >= 40): 402749
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 23.20 MB
- Schedules: 0.47 MB
- Runs: 0.00 MB
- Total: 23.68 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
