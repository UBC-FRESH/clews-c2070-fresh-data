# WS4 tiled 30-m dataset — E5|BC|S23

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `E5|BC|S23` (parent `E5|BC`)
- Tile / row / col: `E5` / 2 / 3
- Province: `BC`
- Centroid: 49.031477, -117.640377
- Allocated harvest: 11155.476091 m3
- Productive subcell area: 13351.356524 ha
- Committed geometry area: 15919.146542 ha
- Clipped inventory geometry: 15919.146542 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 140690
- Blocks: 66033
- Forest area: 12662.10 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 5617
- Scheduled area: 933.84 ha
- Eligible blocks (age class >= 40): 56168
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 2.50 MB
- Schedules: 0.06 MB
- Runs: 0.00 MB
- Total: 2.56 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
