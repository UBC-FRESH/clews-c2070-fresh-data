# WS4 tiled 30-m dataset — T5|NT|S13

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `T5|NT|S13` (parent `T5|NT`)
- Tile / row / col: `T5` / 1 / 3
- Province: `NT`
- Centroid: 67.006151, -135.831063
- Allocated harvest: 0.026255 m3
- Productive subcell area: 27.292541 ha
- Committed geometry area: 382.680838 ha
- Clipped inventory geometry: 382.680838 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1207
- Blocks: 518
- Forest area: 108.63 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 258
- Scheduled area: 42.12 ha
- Eligible blocks (age class >= 40): 258
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 0.09 MB
- Schedules: 0.00 MB
- Runs: 0.00 MB
- Total: 0.09 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
