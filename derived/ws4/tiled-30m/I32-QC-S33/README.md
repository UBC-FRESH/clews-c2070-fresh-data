# WS4 tiled 30-m dataset — I32|QC|S33

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `I32|QC|S33` (parent `I32|QC`)
- Tile / row / col: `I32` / 3 / 3
- Province: `QC`
- Centroid: 51.186344, -58.542494
- Allocated harvest: 1415.424588 m3
- Productive subcell area: 6069.177616 ha
- Committed geometry area: 8619.010669 ha
- Clipped inventory geometry: 8619.010669 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 18534
- Blocks: 14277
- Forest area: 1668.06 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 991
- Scheduled area: 117.54 ha
- Eligible blocks (age class >= 40): 9909
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 0.48 MB
- Schedules: 0.01 MB
- Runs: 0.00 MB
- Total: 0.49 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
