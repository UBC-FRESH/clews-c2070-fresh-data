# WS4 tiled 30-m dataset — B22|ON|S31

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `B22|ON|S31` (parent `B22|ON`)
- Tile / row / col: `B22` / 3 / 1
- Province: `ON`
- Centroid: 47.250855, -84.271112
- Allocated harvest: 65891.015365 m3
- Productive subcell area: 224935.326235 ha
- Committed geometry area: 249891.544441 ha
- Clipped inventory geometry: 249891.544441 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2541187
- Blocks: 646999
- Forest area: 228706.83 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 62041
- Scheduled area: 19720.98 ha
- Eligible blocks (age class >= 40): 620403
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 27.51 MB
- Schedules: 0.73 MB
- Runs: 0.00 MB
- Total: 28.24 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
