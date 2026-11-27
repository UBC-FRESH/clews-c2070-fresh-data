# WS4 tiled 30-m dataset — G27|QC|S23

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `G27|QC|S23` (parent `G27|QC`)
- Tile / row / col: `G27` / 2 / 3
- Province: `QC`
- Centroid: 51.233180, -70.370241
- Allocated harvest: 51730.942415 m3
- Productive subcell area: 184053.046709 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2294099
- Blocks: 725572
- Forest area: 206468.91 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 66495
- Scheduled area: 19190.43 ha
- Eligible blocks (age class >= 40): 664948
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 27.09 MB
- Schedules: 0.79 MB
- Runs: 0.00 MB
- Total: 27.88 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
