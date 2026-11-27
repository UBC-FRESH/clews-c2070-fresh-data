# WS4 tiled 30-m dataset — E31|NB|S21

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `E31|NB|S21` (parent `E31|NB`)
- Tile / row / col: `E31` / 2 / 1
- Province: `NB`
- Centroid: 46.924066, -65.814946
- Allocated harvest: 180857.256320 m3
- Productive subcell area: 225859.355564 ha
- Committed geometry area: 249184.883796 ha
- Clipped inventory geometry: 249184.883796 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2585616
- Blocks: 965959
- Forest area: 232705.44 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 78088
- Scheduled area: 15037.20 ha
- Eligible blocks (age class >= 40): 780875
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 31.73 MB
- Schedules: 0.93 MB
- Runs: 0.00 MB
- Total: 32.66 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
