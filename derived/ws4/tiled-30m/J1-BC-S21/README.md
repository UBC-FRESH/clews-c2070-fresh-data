# WS4 tiled 30-m dataset — J1|BC|S21

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `J1|BC|S21` (parent `J1|BC`)
- Tile / row / col: `J1` / 2 / 1
- Province: `BC`
- Centroid: 52.179801, -131.205127
- Allocated harvest: 39821.277739 m3
- Productive subcell area: 39715.512521 ha
- Committed geometry area: 41317.733196 ha
- Clipped inventory geometry: 41317.733196 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 449804
- Blocks: 241454
- Forest area: 40482.36 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 24013
- Scheduled area: 4043.61 ha
- Eligible blocks (age class >= 40): 240129
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 7.21 MB
- Schedules: 0.28 MB
- Runs: 0.00 MB
- Total: 7.49 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
