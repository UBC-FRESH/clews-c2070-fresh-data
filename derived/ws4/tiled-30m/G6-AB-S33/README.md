# WS4 tiled 30-m dataset — G6|AB|S33

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `G6|AB|S33` (parent `G6|AB`)
- Tile / row / col: `G6` / 3 / 3
- Province: `AB`
- Centroid: 52.288468, -117.394412
- Allocated harvest: 51695.927696 m3
- Productive subcell area: 56232.827585 ha
- Committed geometry area: 171842.029274 ha
- Clipped inventory geometry: 171842.029274 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 510013
- Blocks: 286918
- Forest area: 45901.17 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 26394
- Scheduled area: 4270.50 ha
- Eligible blocks (age class >= 40): 263933
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 8.19 MB
- Schedules: 0.31 MB
- Runs: 0.00 MB
- Total: 8.49 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
