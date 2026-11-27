# WS4 tiled 30-m dataset — D32|NS|S21

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `D32|NS|S21` (parent `D32|NS`)
- Tile / row / col: `D32` / 2 / 1
- Province: `NS`
- Centroid: 45.028548, -64.865255
- Allocated harvest: 45049.052397 m3
- Productive subcell area: 77902.549451 ha
- Committed geometry area: 95663.970995 ha
- Clipped inventory geometry: 95663.970995 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 753864
- Blocks: 270121
- Forest area: 67847.76 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 21276
- Scheduled area: 5414.85 ha
- Eligible blocks (age class >= 40): 212753
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 9.73 MB
- Schedules: 0.25 MB
- Runs: 0.00 MB
- Total: 9.97 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
