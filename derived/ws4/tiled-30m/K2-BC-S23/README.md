# WS4 tiled 30-m dataset — K2|BC|S23

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `K2|BC|S23` (parent `K2|BC`)
- Tile / row / col: `K2` / 2 / 3
- Province: `BC`
- Centroid: 54.411493, -129.341380
- Allocated harvest: 125256.933327 m3
- Productive subcell area: 175668.031403 ha
- Committed geometry area: 249665.038265 ha
- Clipped inventory geometry: 249665.038265 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1166673
- Blocks: 707408
- Forest area: 105000.57 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 65378
- Scheduled area: 9388.08 ha
- Eligible blocks (age class >= 40): 653772
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 18.05 MB
- Schedules: 0.77 MB
- Runs: 0.00 MB
- Total: 18.82 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
