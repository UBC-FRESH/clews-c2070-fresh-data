# WS4 tiled 30-m dataset — J29|NL|S32

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `J29|NL|S32` (parent `J29|NL`)
- Tile / row / col: `J29` / 3 / 2
- Province: `NL`
- Centroid: 54.381138, -63.769437
- Allocated harvest: 6290.379138 m3
- Productive subcell area: 134548.777260 ha
- Committed geometry area: 241585.076244 ha
- Clipped inventory geometry: 241585.076244 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1069016
- Blocks: 542002
- Forest area: 96211.44 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 48139
- Scheduled area: 8370.45 ha
- Eligible blocks (age class >= 40): 481388
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 15.12 MB
- Schedules: 0.57 MB
- Runs: 0.00 MB
- Total: 15.69 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
