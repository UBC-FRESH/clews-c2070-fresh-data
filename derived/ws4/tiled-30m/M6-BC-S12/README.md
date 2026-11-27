# WS4 tiled 30-m dataset — M6|BC|S12

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `M6|BC|S12` (parent `M6|BC`)
- Tile / row / col: `M6` / 1 / 2
- Province: `BC`
- Centroid: 58.826485, -123.228686
- Allocated harvest: 105132.256149 m3
- Productive subcell area: 215827.663959 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2621209
- Blocks: 1068466
- Forest area: 235908.81 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 102927
- Scheduled area: 21394.08 ha
- Eligible blocks (age class >= 40): 1029268
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 33.58 MB
- Schedules: 1.23 MB
- Runs: 0.00 MB
- Total: 34.82 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
