# WS4 tiled 30-m dataset — F3|BC|S21

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `F3|BC|S21` (parent `F3|BC`)
- Tile / row / col: `F3` / 2 / 1
- Province: `BC`
- Centroid: 48.622870, -123.616032
- Allocated harvest: 115276.206516 m3
- Productive subcell area: 114823.690217 ha
- Committed geometry area: 170078.494298 ha
- Clipped inventory geometry: 170078.494298 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1433025
- Blocks: 585385
- Forest area: 128972.25 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 54037
- Scheduled area: 10170.09 ha
- Eligible blocks (age class >= 40): 540365
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 18.68 MB
- Schedules: 0.64 MB
- Runs: 0.00 MB
- Total: 19.32 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
