# WS4 tiled 30-m dataset — J26|QC|S11

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `J26|QC|S11` (parent `J26|QC`)
- Tile / row / col: `J26` / 1 / 1
- Province: `QC`
- Centroid: 55.463000, -71.668044
- Allocated harvest: 13507.774698 m3
- Productive subcell area: 127798.873441 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1098636
- Blocks: 504648
- Forest area: 98877.24 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 37947
- Scheduled area: 7875.72 ha
- Eligible blocks (age class >= 40): 379470
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 14.87 MB
- Schedules: 0.45 MB
- Runs: 0.00 MB
- Total: 15.32 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
