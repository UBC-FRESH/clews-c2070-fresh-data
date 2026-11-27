# WS4 tiled 30-m dataset — I32|QC|S12

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `I32|QC|S12` (parent `I32|QC`)
- Tile / row / col: `I32` / 1 / 2
- Province: `QC`
- Centroid: 50.449499, -59.944484
- Allocated harvest: 21481.799573 m3
- Productive subcell area: 92111.482439 ha
- Committed geometry area: 130810.119612 ha
- Clipped inventory geometry: 130810.119612 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 628232
- Blocks: 284067
- Forest area: 56540.88 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 23535
- Scheduled area: 4936.50 ha
- Eligible blocks (age class >= 40): 235346
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 8.94 MB
- Schedules: 0.27 MB
- Runs: 0.00 MB
- Total: 9.21 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
