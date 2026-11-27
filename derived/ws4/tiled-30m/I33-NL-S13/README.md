# WS4 tiled 30-m dataset — I33|NL|S13

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `I33|NL|S13` (parent `I33|NL`)
- Tile / row / col: `I33` / 1 / 3
- Province: `NL`
- Centroid: 49.401516, -57.478024
- Allocated harvest: 11485.305090 m3
- Productive subcell area: 184407.676588 ha
- Committed geometry area: 248291.372089 ha
- Clipped inventory geometry: 248291.372089 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2104163
- Blocks: 1071864
- Forest area: 189374.67 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 99676
- Scheduled area: 15808.32 ha
- Eligible blocks (age class >= 40): 996760
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 29.55 MB
- Schedules: 1.19 MB
- Runs: 0.00 MB
- Total: 30.74 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
