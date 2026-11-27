# WS4 tiled 30-m dataset — M6|BC|S31

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `M6|BC|S31` (parent `M6|BC`)
- Tile / row / col: `M6` / 3 / 1
- Province: `BC`
- Centroid: 59.451350, -124.825552
- Allocated harvest: 105132.256149 m3
- Productive subcell area: 215827.663959 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2695396
- Blocks: 1255862
- Forest area: 242585.64 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 124116
- Scheduled area: 27588.33 ha
- Eligible blocks (age class >= 40): 1241155
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 37.30 MB
- Schedules: 1.50 MB
- Runs: 0.00 MB
- Total: 38.80 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
