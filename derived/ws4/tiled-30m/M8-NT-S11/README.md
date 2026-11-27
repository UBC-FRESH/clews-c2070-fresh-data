# WS4 tiled 30-m dataset — M8|NT|S11

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `M8|NT|S11` (parent `M8|NT`)
- Tile / row / col: `M8` / 1 / 1
- Province: `NT`
- Centroid: 60.016491, -118.906047
- Allocated harvest: 2.484831 m3
- Productive subcell area: 1786.663134 ha
- Committed geometry area: 4027.173838 ha
- Clipped inventory geometry: 4027.173838 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 11068
- Blocks: 4185
- Forest area: 996.12 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 2166
- Scheduled area: 290.07 ha
- Eligible blocks (age class >= 40): 2166
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 0.24 MB
- Schedules: 0.02 MB
- Runs: 0.00 MB
- Total: 0.26 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
