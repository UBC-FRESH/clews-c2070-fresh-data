# WS4 tiled 30-m dataset — F30|QC|S32

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `F30|QC|S32` (parent `F30|QC`)
- Tile / row / col: `F30` / 3 / 2
- Province: `QC`
- Centroid: 48.926724, -65.828549
- Allocated harvest: 127248.970554 m3
- Productive subcell area: 236152.041553 ha
- Committed geometry area: 249995.731984 ha
- Clipped inventory geometry: 249995.731984 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2659091
- Blocks: 816900
- Forest area: 239318.19 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 68616
- Scheduled area: 20139.93 ha
- Eligible blocks (age class >= 40): 686154
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 30.49 MB
- Schedules: 0.81 MB
- Runs: 0.00 MB
- Total: 31.31 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
