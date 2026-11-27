# WS4 tiled 30-m dataset — F30|NB|S12

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `F30|NB|S12` (parent `F30|NB`)
- Tile / row / col: `F30` / 1 / 2
- Province: `NB`
- Centroid: 47.952734, -66.422762
- Allocated harvest: 53204.739576 m3
- Productive subcell area: 55113.854671 ha
- Committed geometry area: 58197.077978 ha
- Clipped inventory geometry: 58197.077978 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 572949
- Blocks: 185396
- Forest area: 51565.41 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 15395
- Scheduled area: 3750.57 ha
- Eligible blocks (age class >= 40): 153947
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 7.35 MB
- Schedules: 0.18 MB
- Runs: 0.00 MB
- Total: 7.53 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
