# WS4 tiled 30-m dataset — F5|BC|S23

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `F5|BC|S23` (parent `F5|BC`)
- Tile / row / col: `F5` / 2 / 3
- Province: `BC`
- Centroid: 50.066408, -118.469488
- Allocated harvest: 161914.105795 m3
- Productive subcell area: 203427.507706 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2498372
- Blocks: 896961
- Forest area: 224853.48 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 81015
- Scheduled area: 15925.77 ha
- Eligible blocks (age class >= 40): 810142
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 30.21 MB
- Schedules: 0.96 MB
- Runs: 0.00 MB
- Total: 31.18 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
