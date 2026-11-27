# WS4 tiled 30-m dataset — K33|NL|S22

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `K33|NL|S22` (parent `K33|NL`)
- Tile / row / col: `K33` / 2 / 2
- Province: `NL`
- Centroid: 52.213552, -55.676886
- Allocated harvest: 86.694360 m3
- Productive subcell area: 1985.753118 ha
- Committed geometry area: 3068.401425 ha
- Clipped inventory geometry: 3068.401425 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 5855
- Blocks: 4161
- Forest area: 526.95 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 2934
- Scheduled area: 392.13 ha
- Eligible blocks (age class >= 40): 2934
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 0.19 MB
- Schedules: 0.03 MB
- Runs: 0.00 MB
- Total: 0.22 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
