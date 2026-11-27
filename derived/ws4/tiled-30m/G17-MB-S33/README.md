# WS4 tiled 30-m dataset — G17|MB|S33

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `G17|MB|S33` (parent `G17|MB`)
- Tile / row / col: `G17` / 3 / 3
- Province: `MB`
- Centroid: 54.690963, -92.561739
- Allocated harvest: 3383.925516 m3
- Productive subcell area: 94496.613333 ha
- Committed geometry area: 127762.877970 ha
- Clipped inventory geometry: 127762.877970 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1057515
- Blocks: 439721
- Forest area: 95176.35 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 40655
- Scheduled area: 8523.00 ha
- Eligible blocks (age class >= 40): 406542
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 13.76 MB
- Schedules: 0.48 MB
- Runs: 0.00 MB
- Total: 14.24 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
