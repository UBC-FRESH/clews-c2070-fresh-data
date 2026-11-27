# WS4 tiled 30-m dataset — M2|BC|S33

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `M2|BC|S33` (parent `M2|BC`)
- Tile / row / col: `M2` / 3 / 3
- Province: `BC`
- Centroid: 57.189149, -132.128970
- Allocated harvest: 8371.938187 m3
- Productive subcell area: 16565.519922 ha
- Committed geometry area: 78516.306959 ha
- Clipped inventory geometry: 78516.306959 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 28454
- Blocks: 14968
- Forest area: 2560.86 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 1057
- Scheduled area: 234.54 ha
- Eligible blocks (age class >= 40): 10563
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 0.57 MB
- Schedules: 0.01 MB
- Runs: 0.00 MB
- Total: 0.58 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
