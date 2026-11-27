# WS4 tiled 30-m dataset — G29|QC|S11

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `G29|QC|S11` (parent `G29|QC`)
- Tile / row / col: `G29` / 1 / 1
- Province: `QC`
- Centroid: 50.103720, -68.035387
- Allocated harvest: 66866.879214 m3
- Productive subcell area: 202172.598931 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2376986
- Blocks: 802373
- Forest area: 213928.74 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 73468
- Scheduled area: 17327.52 ha
- Eligible blocks (age class >= 40): 734676
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 28.59 MB
- Schedules: 0.87 MB
- Runs: 0.00 MB
- Total: 29.46 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
