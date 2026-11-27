# WS4 tiled 30-m dataset — K32|NL|S32

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `K32|NL|S32` (parent `K32|NL`)
- Tile / row / col: `K32` / 3 / 2
- Province: `NL`
- Centroid: 53.416806, -56.621663
- Allocated harvest: 10782.008272 m3
- Productive subcell area: 196564.425493 ha
- Committed geometry area: 246046.330309 ha
- Clipped inventory geometry: 246046.330309 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2292176
- Blocks: 854666
- Forest area: 206295.84 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 79526
- Scheduled area: 18645.21 ha
- Eligible blocks (age class >= 40): 795256
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 28.57 MB
- Schedules: 0.94 MB
- Runs: 0.00 MB
- Total: 29.52 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
