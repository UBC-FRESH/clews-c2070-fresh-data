# WS4 tiled 30-m dataset — G24|QC|S11

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `G24|QC|S11` (parent `G24|QC`)
- Tile / row / col: `G24` / 1 / 1
- Province: `QC`
- Centroid: 52.406831, -78.208131
- Allocated harvest: 27192.474320 m3
- Productive subcell area: 131785.074927 ha
- Committed geometry area: 227218.443522 ha
- Clipped inventory geometry: 227218.443522 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1086012
- Blocks: 444906
- Forest area: 97741.08 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 33587
- Scheduled area: 6383.25 ha
- Eligible blocks (age class >= 40): 335867
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 13.99 MB
- Schedules: 0.40 MB
- Runs: 0.00 MB
- Total: 14.38 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
