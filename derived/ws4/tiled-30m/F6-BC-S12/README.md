# WS4 tiled 30-m dataset — F6|BC|S12

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `F6|BC|S12` (parent `F6|BC`)
- Tile / row / col: `F6` / 1 / 2
- Province: `BC`
- Centroid: 49.958739, -116.912616
- Allocated harvest: 138342.879396 m3
- Productive subcell area: 175902.532281 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1900741
- Blocks: 962726
- Forest area: 171066.69 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 88968
- Scheduled area: 14266.26 ha
- Eligible blocks (age class >= 40): 889675
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 26.69 MB
- Schedules: 1.06 MB
- Runs: 0.00 MB
- Total: 27.75 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
