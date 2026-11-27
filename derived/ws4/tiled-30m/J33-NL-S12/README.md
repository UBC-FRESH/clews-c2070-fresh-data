# WS4 tiled 30-m dataset — J33|NL|S12

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `J33|NL|S12` (parent `J33|NL`)
- Tile / row / col: `J33` / 1 / 2
- Province: `NL`
- Centroid: 50.756825, -56.838540
- Allocated harvest: 6595.826766 m3
- Productive subcell area: 139341.023912 ha
- Committed geometry area: 209984.548153 ha
- Clipped inventory geometry: 209984.548153 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1585012
- Blocks: 895707
- Forest area: 142651.08 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 81986
- Scheduled area: 12540.24 ha
- Eligible blocks (age class >= 40): 819856
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 23.61 MB
- Schedules: 0.97 MB
- Runs: 0.00 MB
- Total: 24.58 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
