# WS4 tiled 30-m dataset — G29|QC|S31

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `G29|QC|S31` (parent `G29|QC`)
- Tile / row / col: `G29` / 3 / 1
- Province: `QC`
- Centroid: 50.925990, -67.446191
- Allocated harvest: 66866.879214 m3
- Productive subcell area: 202172.598931 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2364781
- Blocks: 595099
- Forest area: 212830.29 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 49272
- Scheduled area: 13832.37 ha
- Eligible blocks (age class >= 40): 492714
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 25.66 MB
- Schedules: 0.58 MB
- Runs: 0.00 MB
- Total: 26.25 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
