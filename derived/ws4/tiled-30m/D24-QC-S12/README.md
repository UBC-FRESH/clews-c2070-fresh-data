# WS4 tiled 30-m dataset — D24|QC|S12

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `D24|QC|S12` (parent `D24|QC`)
- Tile / row / col: `D24` / 1 / 2
- Province: `QC`
- Centroid: 48.355680, -79.163924
- Allocated harvest: 80035.188913 m3
- Productive subcell area: 201754.536118 ha
- Committed geometry area: 245727.292253 ha
- Clipped inventory geometry: 245727.292253 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2223946
- Blocks: 923271
- Forest area: 200155.14 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 83416
- Scheduled area: 16952.76 ha
- Eligible blocks (age class >= 40): 834151
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 28.93 MB
- Schedules: 0.99 MB
- Runs: 0.00 MB
- Total: 29.92 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
