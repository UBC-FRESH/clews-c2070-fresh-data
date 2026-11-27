# WS4 tiled 30-m dataset — L9|AB|S21

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `L9|AB|S21` (parent `L9|AB`)
- Tile / row / col: `L9` / 2 / 1
- Province: `AB`
- Centroid: 59.362866, -115.906614
- Allocated harvest: 98025.289357 m3
- Productive subcell area: 196257.628929 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2349223
- Blocks: 532981
- Forest area: 211430.07 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 49033
- Scheduled area: 18180.36 ha
- Eligible blocks (age class >= 40): 490328
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 23.46 MB
- Schedules: 0.58 MB
- Runs: 0.00 MB
- Total: 24.04 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
