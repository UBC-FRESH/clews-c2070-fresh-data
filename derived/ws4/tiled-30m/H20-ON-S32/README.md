# WS4 tiled 30-m dataset — H20|ON|S32

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `H20|ON|S32` (parent `H20|ON`)
- Tile / row / col: `H20` / 3 / 2
- Province: `ON`
- Centroid: 55.534551, -85.925626
- Allocated harvest: 2410.891740 m3
- Productive subcell area: 42491.369840 ha
- Committed geometry area: 94203.146821 ha
- Clipped inventory geometry: 94203.146821 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 355522
- Blocks: 150271
- Forest area: 31996.98 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 12128
- Scheduled area: 2783.70 ha
- Eligible blocks (age class >= 40): 121276
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 5.42 MB
- Schedules: 0.14 MB
- Runs: 0.00 MB
- Total: 5.56 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
