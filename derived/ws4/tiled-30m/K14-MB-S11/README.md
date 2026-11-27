# WS4 tiled 30-m dataset — K14|MB|S11

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `K14|MB|S11` (parent `K14|MB`)
- Tile / row / col: `K14` / 1 / 1
- Province: `MB`
- Centroid: 59.064611, -101.742583
- Allocated harvest: 1245.462756 m3
- Productive subcell area: 74947.450214 ha
- Committed geometry area: 147917.680593 ha
- Clipped inventory geometry: 147917.680593 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 903084
- Blocks: 282334
- Forest area: 81277.56 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 20477
- Scheduled area: 5138.19 ha
- Eligible blocks (age class >= 40): 204763
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 10.57 MB
- Schedules: 0.24 MB
- Runs: 0.00 MB
- Total: 10.81 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
