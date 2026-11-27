# WS4 tiled 30-m dataset — V6|YT|S21

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `V6|YT|S21` (parent `V6|YT`)
- Tile / row / col: `V6` / 2 / 1
- Province: `YT`
- Centroid: 69.442214, -140.359029
- Allocated harvest: 9.031469 m3
- Productive subcell area: 7822.654734 ha
- Committed geometry area: 179482.106970 ha
- Clipped inventory geometry: 179482.106970 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 10644
- Blocks: 7195
- Forest area: 957.96 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 1644
- Scheduled area: 201.42 ha
- Eligible blocks (age class >= 40): 1644
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 0.28 MB
- Schedules: 0.02 MB
- Runs: 0.00 MB
- Total: 0.30 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
