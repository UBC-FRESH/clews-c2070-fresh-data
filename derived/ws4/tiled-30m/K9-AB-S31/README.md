# WS4 tiled 30-m dataset — K9|AB|S31

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `K9|AB|S31` (parent `K9|AB`)
- Tile / row / col: `K9` / 3 / 1
- Province: `AB`
- Centroid: 58.488691, -115.338429
- Allocated harvest: 136547.554935 m3
- Productive subcell area: 212379.340034 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2403196
- Blocks: 1127042
- Forest area: 216287.64 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 105342
- Scheduled area: 19234.98 ha
- Eligible blocks (age class >= 40): 1053417
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 33.06 MB
- Schedules: 1.27 MB
- Runs: 0.00 MB
- Total: 34.33 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
