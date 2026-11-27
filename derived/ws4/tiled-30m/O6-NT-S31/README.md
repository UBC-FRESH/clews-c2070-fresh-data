# WS4 tiled 30-m dataset — O6|NT|S31

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `O6|NT|S31` (parent `O6|NT`)
- Tile / row / col: `O6` / 3 / 1
- Province: `NT`
- Centroid: 61.897838, -127.484137
- Allocated harvest: 101.797925 m3
- Productive subcell area: 122838.100117 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1201196
- Blocks: 544976
- Forest area: 108107.64 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 47966
- Scheduled area: 9242.19 ha
- Eligible blocks (age class >= 40): 479651
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 16.53 MB
- Schedules: 0.57 MB
- Runs: 0.00 MB
- Total: 17.09 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
