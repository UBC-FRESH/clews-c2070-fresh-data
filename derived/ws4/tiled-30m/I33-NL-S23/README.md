# WS4 tiled 30-m dataset — I33|NL|S23

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `I33|NL|S23` (parent `I33|NL`)
- Tile / row / col: `I33` / 2 / 3
- Province: `NL`
- Centroid: 49.774436, -57.123139
- Allocated harvest: 10632.366088 m3
- Productive subcell area: 170712.916336 ha
- Committed geometry area: 229852.384752 ha
- Clipped inventory geometry: 229852.384752 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2048301
- Blocks: 1133050
- Forest area: 184347.09 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 108705
- Scheduled area: 16430.40 ha
- Eligible blocks (age class >= 40): 1087043
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 30.10 MB
- Schedules: 1.31 MB
- Runs: 0.00 MB
- Total: 31.41 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
