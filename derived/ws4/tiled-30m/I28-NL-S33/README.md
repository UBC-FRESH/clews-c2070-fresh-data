# WS4 tiled 30-m dataset — I28|NL|S33

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `I28|NL|S33` (parent `I28|NL`)
- Tile / row / col: `I28` / 3 / 3
- Province: `NL`
- Centroid: 53.584607, -66.211010
- Allocated harvest: 5916.795296 m3
- Productive subcell area: 133062.580942 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1704307
- Blocks: 594159
- Forest area: 153387.63 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 54436
- Scheduled area: 14751.27 ha
- Eligible blocks (age class >= 40): 544360
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 20.73 MB
- Schedules: 0.64 MB
- Runs: 0.00 MB
- Total: 21.38 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
