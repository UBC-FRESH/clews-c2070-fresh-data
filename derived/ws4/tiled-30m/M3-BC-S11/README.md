# WS4 tiled 30-m dataset — M3|BC|S11

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `M3|BC|S11` (parent `M3|BC`)
- Tile / row / col: `M3` / 1 / 1
- Province: `BC`
- Centroid: 56.613990, -130.763468
- Allocated harvest: 41712.759083 m3
- Productive subcell area: 110602.966267 ha
- Committed geometry area: 240278.500358 ha
- Clipped inventory geometry: 240278.500358 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1181381
- Blocks: 630936
- Forest area: 106324.29 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 58501
- Scheduled area: 9507.96 ha
- Eligible blocks (age class >= 40): 585008
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 17.36 MB
- Schedules: 0.69 MB
- Runs: 0.00 MB
- Total: 18.05 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
