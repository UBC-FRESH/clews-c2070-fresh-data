# WS4 tiled 30-m dataset — F30|QC|S21

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `F30|QC|S21` (parent `F30|QC`)
- Tile / row / col: `F30` / 2 / 1
- Province: `QC`
- Centroid: 48.718469, -66.737692
- Allocated harvest: 127251.142994 m3
- Productive subcell area: 236156.073225 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2655745
- Blocks: 872785
- Forest area: 239017.05 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 73230
- Scheduled area: 18070.29 ha
- Eligible blocks (age class >= 40): 732291
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 31.21 MB
- Schedules: 0.87 MB
- Runs: 0.00 MB
- Total: 32.08 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
