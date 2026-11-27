# WS4 tiled 30-m dataset — J29|QC|S32

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `J29|QC|S32` (parent `J29|QC`)
- Tile / row / col: `J29` / 3 / 2
- Province: `QC`
- Centroid: 54.645675, -63.901357
- Allocated harvest: 654.785985 m3
- Productive subcell area: 4071.799665 ha
- Committed geometry area: 8414.923756 ha
- Clipped inventory geometry: 8414.923756 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 52728
- Blocks: 32634
- Forest area: 4745.52 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 2915
- Scheduled area: 417.78 ha
- Eligible blocks (age class >= 40): 29142
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 1.11 MB
- Schedules: 0.03 MB
- Runs: 0.00 MB
- Total: 1.14 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
