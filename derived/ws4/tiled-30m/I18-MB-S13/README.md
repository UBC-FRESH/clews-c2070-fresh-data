# WS4 tiled 30-m dataset — I18|MB|S13

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `I18|MB|S13` (parent `I18|MB`)
- Tile / row / col: `I18` / 1 / 3
- Province: `MB`
- Centroid: 56.436560, -89.943009
- Allocated harvest: 931.355674 m3
- Productive subcell area: 71967.176071 ha
- Committed geometry area: 133755.706984 ha
- Clipped inventory geometry: 133755.706984 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 669956
- Blocks: 239502
- Forest area: 60296.04 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 16237
- Scheduled area: 4160.61 ha
- Eligible blocks (age class >= 40): 162365
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 8.47 MB
- Schedules: 0.19 MB
- Runs: 0.00 MB
- Total: 8.65 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
