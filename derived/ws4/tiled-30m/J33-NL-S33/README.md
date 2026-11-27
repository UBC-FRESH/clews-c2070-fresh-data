# WS4 tiled 30-m dataset — J33|NL|S33

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `J33|NL|S33` (parent `J33|NL`)
- Tile / row / col: `J33` / 3 / 3
- Province: `NL`
- Centroid: 51.369428, -55.657346
- Allocated harvest: 1471.961059 m3
- Productive subcell area: 31096.110973 ha
- Committed geometry area: 46861.309244 ha
- Clipped inventory geometry: 46861.309244 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 316705
- Blocks: 197799
- Forest area: 28503.45 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 18087
- Scheduled area: 2585.70 ha
- Eligible blocks (age class >= 40): 180869
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 5.76 MB
- Schedules: 0.21 MB
- Runs: 0.00 MB
- Total: 5.97 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
