# WS4 tiled 30-m dataset — J1|BC|S11

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `J1|BC|S11` (parent `J1|BC`)
- Tile / row / col: `J1` / 1 / 1
- Province: `BC`
- Centroid: 51.910552, -130.982469
- Allocated harvest: 4.848846 m3
- Productive subcell area: 4.835967 ha
- Committed geometry area: 5.031062 ha
- Clipped inventory geometry: 5.031062 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 43
- Blocks: 33
- Forest area: 3.87 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 30
- Scheduled area: 3.42 ha
- Eligible blocks (age class >= 40): 30
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 0.07 MB
- Schedules: 0.00 MB
- Runs: 0.00 MB
- Total: 0.07 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
