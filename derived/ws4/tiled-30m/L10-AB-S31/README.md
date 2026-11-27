# WS4 tiled 30-m dataset — L10|AB|S31

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `L10|AB|S31` (parent `L10|AB`)
- Tile / row / col: `L10` / 3 / 1
- Province: `AB`
- Centroid: 59.979395, -113.752614
- Allocated harvest: 3121.869503 m3
- Productive subcell area: 6666.124886 ha
- Committed geometry area: 8304.748162 ha
- Clipped inventory geometry: 8304.748162 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 72651
- Blocks: 20982
- Forest area: 6538.59 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 1424
- Scheduled area: 272.43 ha
- Eligible blocks (age class >= 40): 14236
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 1.05 MB
- Schedules: 0.01 MB
- Runs: 0.00 MB
- Total: 1.07 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
