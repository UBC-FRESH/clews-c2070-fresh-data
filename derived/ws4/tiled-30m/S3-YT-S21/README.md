# WS4 tiled 30-m dataset — S3|YT|S21

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `S3|YT|S21` (parent `S3|YT`)
- Tile / row / col: `S3` / 2 / 1
- Province: `YT`
- Centroid: 63.626274, -140.876230
- Allocated harvest: 64.410871 m3
- Productive subcell area: 26567.856404 ha
- Committed geometry area: 34065.045875 ha
- Clipped inventory geometry: 34065.045875 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 316038
- Blocks: 72609
- Forest area: 28443.42 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 6211
- Scheduled area: 2135.97 ha
- Eligible blocks (age class >= 40): 62109
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 3.55 MB
- Schedules: 0.07 MB
- Runs: 0.00 MB
- Total: 3.62 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
