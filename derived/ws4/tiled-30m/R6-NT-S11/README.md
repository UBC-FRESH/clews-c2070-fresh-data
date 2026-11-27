# WS4 tiled 30-m dataset — R6|NT|S11

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `R6|NT|S11` (parent `R6|NT`)
- Tile / row / col: `R6` / 1 / 1
- Province: `NT`
- Centroid: 64.684204, -131.178446
- Allocated harvest: 63.222842 m3
- Productive subcell area: 92102.728269 ha
- Committed geometry area: 243272.601015 ha
- Clipped inventory geometry: 243272.601015 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 388822
- Blocks: 197180
- Forest area: 34993.98 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 13472
- Scheduled area: 2358.45 ha
- Eligible blocks (age class >= 40): 134712
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 6.21 MB
- Schedules: 0.15 MB
- Runs: 0.00 MB
- Total: 6.37 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
