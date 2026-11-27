# WS4 tiled 30-m dataset — O12|NT|S31

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `O12|NT|S31` (parent `O12|NT`)
- Tile / row / col: `O12` / 3 / 1
- Province: `NT`
- Centroid: 64.959374, -110.139768
- Allocated harvest: 2.207458 m3
- Productive subcell area: 4732.239619 ha
- Committed geometry area: 237794.256171 ha
- Clipped inventory geometry: 237794.256171 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 50605
- Blocks: 41044
- Forest area: 4554.45 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 1000
- Scheduled area: 95.31 ha
- Eligible blocks (age class >= 40): 9993
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 1.21 MB
- Schedules: 0.01 MB
- Runs: 0.00 MB
- Total: 1.22 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
