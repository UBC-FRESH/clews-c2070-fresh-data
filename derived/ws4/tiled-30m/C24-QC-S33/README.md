# WS4 tiled 30-m dataset — C24|QC|S33

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `C24|QC|S33` (parent `C24|QC`)
- Tile / row / col: `C24` / 3 / 3
- Province: `QC`
- Centroid: 47.807934, -78.690074
- Allocated harvest: 109548.818649 m3
- Productive subcell area: 196565.219679 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2294998
- Blocks: 924241
- Forest area: 206549.82 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 81465
- Scheduled area: 16585.74 ha
- Eligible blocks (age class >= 40): 814646
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 29.83 MB
- Schedules: 0.97 MB
- Runs: 0.00 MB
- Total: 30.80 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
