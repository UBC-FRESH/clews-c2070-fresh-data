# WS4 tiled 30-m dataset — L27|QC|S33

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `L27|QC|S33` (parent `L27|QC`)
- Tile / row / col: `L27` / 3 / 3
- Province: `QC`
- Centroid: 57.892087, -65.140672
- Allocated harvest: 14919.959864 m3
- Productive subcell area: 91923.631808 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 187454
- Blocks: 96659
- Forest area: 16870.86 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 6549
- Scheduled area: 1195.83 ha
- Eligible blocks (age class >= 40): 65485
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 3.36 MB
- Schedules: 0.07 MB
- Runs: 0.00 MB
- Total: 3.44 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
