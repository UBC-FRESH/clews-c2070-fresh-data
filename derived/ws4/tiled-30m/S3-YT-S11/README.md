# WS4 tiled 30-m dataset — S3|YT|S11

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `S3|YT|S11` (parent `S3|YT`)
- Tile / row / col: `S3` / 1 / 1
- Province: `YT`
- Centroid: 63.284141, -140.590724
- Allocated harvest: 402.889565 m3
- Productive subcell area: 166181.762057 ha
- Committed geometry area: 213076.631475 ha
- Clipped inventory geometry: 213076.631475 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2074100
- Blocks: 630359
- Forest area: 186669.00 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 57033
- Scheduled area: 12414.42 ha
- Eligible blocks (age class >= 40): 570323
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 22.67 MB
- Schedules: 0.67 MB
- Runs: 0.00 MB
- Total: 23.35 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
