# WS4 tiled 30-m dataset — J1|BC|S32

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `J1|BC|S32` (parent `J1|BC`)
- Tile / row / col: `J1` / 3 / 2
- Province: `BC`
- Centroid: 52.676317, -131.503601
- Allocated harvest: 13900.148008 m3
- Productive subcell area: 13863.229249 ha
- Committed geometry area: 14422.505740 ha
- Clipped inventory geometry: 14422.505740 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 156969
- Blocks: 74262
- Forest area: 14127.21 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 7363
- Scheduled area: 1253.97 ha
- Eligible blocks (age class >= 40): 73627
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 2.70 MB
- Schedules: 0.08 MB
- Runs: 0.00 MB
- Total: 2.78 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
