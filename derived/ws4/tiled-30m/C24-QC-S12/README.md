# WS4 tiled 30-m dataset — C24|QC|S12

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `C24|QC|S12` (parent `C24|QC`)
- Tile / row / col: `C24` / 1 / 2
- Province: `QC`
- Centroid: 47.138719, -79.360212
- Allocated harvest: 10900.383500 m3
- Productive subcell area: 19558.734668 ha
- Committed geometry area: 24875.629957 ha
- Clipped inventory geometry: 24875.629957 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 200907
- Blocks: 71531
- Forest area: 18081.63 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 6177
- Scheduled area: 1396.80 ha
- Eligible blocks (age class >= 40): 61766
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 3.00 MB
- Schedules: 0.07 MB
- Runs: 0.00 MB
- Total: 3.07 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
