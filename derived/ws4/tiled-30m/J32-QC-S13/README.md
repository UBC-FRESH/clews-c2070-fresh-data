# WS4 tiled 30-m dataset — J32|QC|S13

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `J32|QC|S13` (parent `J32|QC`)
- Tile / row / col: `J32` / 1 / 3
- Province: `QC`
- Centroid: 51.392313, -58.167053
- Allocated harvest: 14440.970261 m3
- Productive subcell area: 71511.328524 ha
- Committed geometry area: 100677.361662 ha
- Clipped inventory geometry: 100677.361662 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 553969
- Blocks: 253132
- Forest area: 49857.21 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 20474
- Scheduled area: 4356.00 ha
- Eligible blocks (age class >= 40): 204735
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 8.04 MB
- Schedules: 0.24 MB
- Runs: 0.00 MB
- Total: 8.27 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
