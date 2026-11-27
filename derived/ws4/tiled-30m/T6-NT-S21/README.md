# WS4 tiled 30-m dataset — T6|NT|S21

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `T6|NT|S21` (parent `T6|NT`)
- Tile / row / col: `T6` / 2 / 1
- Province: `NT`
- Centroid: 67.340026, -135.632606
- Allocated harvest: 147.094671 m3
- Productive subcell area: 128299.654272 ha
- Committed geometry area: 223680.399248 ha
- Clipped inventory geometry: 223680.399248 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 643806
- Blocks: 293400
- Forest area: 57942.54 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 16714
- Scheduled area: 2952.81 ha
- Eligible blocks (age class >= 40): 167136
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 9.14 MB
- Schedules: 0.20 MB
- Runs: 0.00 MB
- Total: 9.34 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
