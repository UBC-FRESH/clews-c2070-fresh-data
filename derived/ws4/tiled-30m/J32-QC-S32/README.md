# WS4 tiled 30-m dataset — J32|QC|S32

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `J32|QC|S32` (parent `J32|QC`)
- Tile / row / col: `J32` / 3 / 2
- Province: `QC`
- Centroid: 51.989363, -57.788832
- Allocated harvest: 110.440650 m3
- Productive subcell area: 546.899377 ha
- Committed geometry area: 769.953342 ha
- Clipped inventory geometry: 769.953342 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 8384
- Blocks: 2095
- Forest area: 754.56 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 2016
- Scheduled area: 695.16 ha
- Eligible blocks (age class >= 40): 2016
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 0.18 MB
- Schedules: 0.02 MB
- Runs: 0.00 MB
- Total: 0.20 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
