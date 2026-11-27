# WS4 tiled 30-m dataset — E29|QC|S11

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `E29|QC|S11` (parent `E29|QC`)
- Tile / row / col: `E29` / 1 / 1
- Province: `QC`
- Centroid: 47.593154, -69.583145
- Allocated harvest: 79609.262255 m3
- Productive subcell area: 136885.004578 ha
- Committed geometry area: 166091.753057 ha
- Clipped inventory geometry: 166091.753057 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1375232
- Blocks: 531207
- Forest area: 123770.88 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 44809
- Scheduled area: 9778.50 ha
- Eligible blocks (age class >= 40): 448087
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 17.66 MB
- Schedules: 0.53 MB
- Runs: 0.00 MB
- Total: 18.19 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
