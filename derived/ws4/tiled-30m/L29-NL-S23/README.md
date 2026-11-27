# WS4 tiled 30-m dataset — L29|NL|S23

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `L29|NL|S23` (parent `L29|NL`)
- Tile / row / col: `L29` / 2 / 3
- Province: `NL`
- Centroid: 56.101677, -61.241703
- Allocated harvest: 2293.455333 m3
- Productive subcell area: 30228.679150 ha
- Committed geometry area: 79516.264080 ha
- Clipped inventory geometry: 79516.264080 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 382436
- Blocks: 137752
- Forest area: 34419.24 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 9579
- Scheduled area: 2476.98 ha
- Eligible blocks (age class >= 40): 95784
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 5.30 MB
- Schedules: 0.11 MB
- Runs: 0.00 MB
- Total: 5.41 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
