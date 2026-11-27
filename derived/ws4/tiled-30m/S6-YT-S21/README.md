# WS4 tiled 30-m dataset — S6|YT|S21

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `S6|YT|S21` (parent `S6|YT`)
- Tile / row / col: `S6` / 2 / 1
- Province: `YT`
- Centroid: 66.193123, -133.919072
- Allocated harvest: 155.147201 m3
- Productive subcell area: 85168.870784 ha
- Committed geometry area: 122983.319207 ha
- Clipped inventory geometry: 122983.319207 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 938872
- Blocks: 271367
- Forest area: 84498.48 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 20704
- Scheduled area: 5546.34 ha
- Eligible blocks (age class >= 40): 207039
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 10.55 MB
- Schedules: 0.24 MB
- Runs: 0.00 MB
- Total: 10.79 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
