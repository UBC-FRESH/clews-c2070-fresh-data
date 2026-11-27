# WS4 tiled 30-m dataset — G34|NL|S32

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `G34|NL|S32` (parent `G34|NL`)
- Tile / row / col: `G34` / 3 / 2
- Province: `NL`
- Centroid: 47.669720, -57.879826
- Allocated harvest: 146.161379 m3
- Productive subcell area: 2202.296564 ha
- Committed geometry area: 4799.578194 ha
- Clipped inventory geometry: 4799.578194 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 8640
- Blocks: 6195
- Forest area: 777.60 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 3784
- Scheduled area: 476.73 ha
- Eligible blocks (age class >= 40): 3784
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 0.25 MB
- Schedules: 0.04 MB
- Runs: 0.00 MB
- Total: 0.29 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
