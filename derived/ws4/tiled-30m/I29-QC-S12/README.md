# WS4 tiled 30-m dataset — I29|QC|S12

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `I29|QC|S12` (parent `I29|QC`)
- Tile / row / col: `I29` / 1 / 2
- Province: `QC`
- Centroid: 52.105098, -65.498532
- Allocated harvest: 4.659293 m3
- Productive subcell area: 25.571138 ha
- Committed geometry area: 39.633623 ha
- Clipped inventory geometry: 39.633623 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 440
- Blocks: 262
- Forest area: 39.60 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 258
- Scheduled area: 39.06 ha
- Eligible blocks (age class >= 40): 258
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 0.08 MB
- Schedules: 0.00 MB
- Runs: 0.00 MB
- Total: 0.08 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
