# WS4 tiled 30-m dataset — D27|QC|S32

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `D27|QC|S32` (parent `D27|QC`)
- Tile / row / col: `D27` / 3 / 2
- Province: `QC`
- Centroid: 48.028666, -73.006724
- Allocated harvest: 120307.451326 m3
- Productive subcell area: 223494.001956 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2465920
- Blocks: 817050
- Forest area: 221932.80 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 66964
- Scheduled area: 14678.19 ha
- Eligible blocks (age class >= 40): 669635
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 29.37 MB
- Schedules: 0.79 MB
- Runs: 0.00 MB
- Total: 30.17 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
