# WS4 tiled 30-m dataset — F7|AB|S31

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `F7|AB|S31` (parent `F7|AB`)
- Tile / row / col: `F7` / 3 / 1
- Province: `AB`
- Centroid: 51.212566, -115.875188
- Allocated harvest: 41223.881236 m3
- Productive subcell area: 47128.072496 ha
- Committed geometry area: 82805.714310 ha
- Clipped inventory geometry: 82805.714310 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 561298
- Blocks: 305992
- Forest area: 50516.82 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 29232
- Scheduled area: 5048.19 ha
- Eligible blocks (age class >= 40): 292320
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 8.86 MB
- Schedules: 0.34 MB
- Runs: 0.00 MB
- Total: 9.20 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
