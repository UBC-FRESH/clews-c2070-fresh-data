# WS4 tiled 30-m dataset — J10|AB|S33

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `J10|AB|S33` (parent `J10|AB`)
- Tile / row / col: `J10` / 3 / 3
- Province: `AB`
- Centroid: 57.802329, -110.439716
- Allocated harvest: 61912.430434 m3
- Productive subcell area: 210953.509718 ha
- Committed geometry area: 243726.752575 ha
- Clipped inventory geometry: 243726.752575 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2152029
- Blocks: 458116
- Forest area: 193682.61 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 33231
- Scheduled area: 7513.20 ha
- Eligible blocks (age class >= 40): 332308
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 20.26 MB
- Schedules: 0.39 MB
- Runs: 0.00 MB
- Total: 20.65 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
