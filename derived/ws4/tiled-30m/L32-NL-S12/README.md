# WS4 tiled 30-m dataset — L32|NL|S12

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `L32|NL|S12` (parent `L32|NL`)
- Tile / row / col: `L32` / 1 / 2
- Province: `NL`
- Centroid: 53.562192, -56.139543
- Allocated harvest: 708.780096 m3
- Productive subcell area: 12646.226394 ha
- Committed geometry area: 24268.822082 ha
- Clipped inventory geometry: 24268.822082 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 82694
- Blocks: 54635
- Forest area: 7442.46 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 3614
- Scheduled area: 460.26 ha
- Eligible blocks (age class >= 40): 36135
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 1.78 MB
- Schedules: 0.04 MB
- Runs: 0.00 MB
- Total: 1.82 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
