# WS4 tiled 30-m dataset — G10|AB|S31

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `G10|AB|S31` (parent `G10|AB`)
- Tile / row / col: `G10` / 3 / 1
- Province: `AB`
- Centroid: 53.576406, -110.320945
- Allocated harvest: 5612.125470 m3
- Productive subcell area: 12543.374210 ha
- Committed geometry area: 209963.960719 ha
- Clipped inventory geometry: 209963.960719 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 429731
- Blocks: 181297
- Forest area: 38675.79 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 11360
- Scheduled area: 2693.25 ha
- Eligible blocks (age class >= 40): 113597
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 6.25 MB
- Schedules: 0.13 MB
- Runs: 0.00 MB
- Total: 6.38 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
