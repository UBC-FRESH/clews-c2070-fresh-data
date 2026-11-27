# WS4 tiled 30-m dataset — I32|QC|S23

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `I32|QC|S23` (parent `I32|QC`)
- Tile / row / col: `I32` / 2 / 3
- Province: `QC`
- Centroid: 50.751634, -59.028038
- Allocated harvest: 232.469285 m3
- Productive subcell area: 996.801521 ha
- Committed geometry area: 1415.586013 ha
- Clipped inventory geometry: 1415.586013 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 4003
- Blocks: 2634
- Forest area: 360.27 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 1921
- Scheduled area: 275.31 ha
- Eligible blocks (age class >= 40): 1921
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 0.15 MB
- Schedules: 0.02 MB
- Runs: 0.00 MB
- Total: 0.17 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
