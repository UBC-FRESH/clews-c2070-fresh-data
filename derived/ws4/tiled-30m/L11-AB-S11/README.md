# WS4 tiled 30-m dataset — L11|AB|S11

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `L11|AB|S11` (parent `L11|AB`)
- Tile / row / col: `L11` / 1 / 1
- Province: `AB`
- Centroid: 59.704262, -110.441135
- Allocated harvest: 38893.155910 m3
- Productive subcell area: 184185.869458 ha
- Committed geometry area: 238486.365743 ha
- Clipped inventory geometry: 238486.365743 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2023977
- Blocks: 353407
- Forest area: 182157.93 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 18653
- Scheduled area: 7998.21 ha
- Eligible blocks (age class >= 40): 186523
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 17.89 MB
- Schedules: 0.22 MB
- Runs: 0.00 MB
- Total: 18.10 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
