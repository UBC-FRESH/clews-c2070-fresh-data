# WS4 tiled 30-m dataset — G10|AB|S11

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `G10|AB|S11` (parent `G10|AB`)
- Tile / row / col: `G10` / 1 / 1
- Province: `AB`
- Centroid: 52.679593, -110.141273
- Allocated harvest: 2402.149711 m3
- Productive subcell area: 5368.921791 ha
- Committed geometry area: 89870.561558 ha
- Clipped inventory geometry: 89870.561558 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 172388
- Blocks: 66597
- Forest area: 15514.92 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 2846
- Scheduled area: 926.55 ha
- Eligible blocks (age class >= 40): 28459
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 2.64 MB
- Schedules: 0.03 MB
- Runs: 0.00 MB
- Total: 2.67 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
