# WS4 tiled 30-m dataset — M14|NT|S32

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `M14|NT|S32` (parent `M14|NT`)
- Tile / row / col: `M14` / 3 / 2
- Province: `NT`
- Centroid: 62.782664, -102.152196
- Allocated harvest: 3.122839 m3
- Productive subcell area: 8155.797684 ha
- Committed geometry area: 74956.206035 ha
- Clipped inventory geometry: 74956.206035 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 11697
- Blocks: 10177
- Forest area: 1052.73 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 3391
- Scheduled area: 345.51 ha
- Eligible blocks (age class >= 40): 3391
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 0.34 MB
- Schedules: 0.03 MB
- Runs: 0.00 MB
- Total: 0.37 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
