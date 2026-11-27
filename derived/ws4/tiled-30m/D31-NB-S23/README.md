# WS4 tiled 30-m dataset — D31|NB|S23

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `D31|NB|S23` (parent `D31|NB`)
- Tile / row / col: `D31` / 2 / 3
- Province: `NB`
- Centroid: 45.427693, -65.625439
- Allocated harvest: 87706.969126 m3
- Productive subcell area: 97780.855933 ha
- Committed geometry area: 111828.089597 ha
- Clipped inventory geometry: 111828.089597 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1140408
- Blocks: 453164
- Forest area: 102636.72 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 39302
- Scheduled area: 8105.58 ha
- Eligible blocks (age class >= 40): 393014
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 14.77 MB
- Schedules: 0.46 MB
- Runs: 0.00 MB
- Total: 15.23 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
