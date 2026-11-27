# WS4 tiled 30-m dataset — L24|QC|S21

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `L24|QC|S21` (parent `L24|QC`)
- Tile / row / col: `L24` / 2 / 1
- Province: `QC`
- Centroid: 59.427305, -74.467443
- Allocated harvest: 7.876151 m3
- Productive subcell area: 39.741204 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 53637
- Blocks: 43527
- Forest area: 4827.33 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 3345
- Scheduled area: 326.97 ha
- Eligible blocks (age class >= 40): 3345
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 1.26 MB
- Schedules: 0.04 MB
- Runs: 0.00 MB
- Total: 1.29 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
