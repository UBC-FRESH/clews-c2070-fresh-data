# WS4 tiled 30-m dataset — L26|QC|S33

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `L26|QC|S33` (parent `L26|QC`)
- Tile / row / col: `L26` / 3 / 3
- Province: `QC`
- Centroid: 58.302445, -67.261513
- Allocated harvest: 2583.672652 m3
- Productive subcell area: 14789.425394 ha
- Committed geometry area: 39765.127949 ha
- Clipped inventory geometry: 39765.127949 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 50315
- Blocks: 26467
- Forest area: 4528.35 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 1504
- Scheduled area: 367.74 ha
- Eligible blocks (age class >= 40): 15034
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 0.96 MB
- Schedules: 0.02 MB
- Runs: 0.00 MB
- Total: 0.97 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
