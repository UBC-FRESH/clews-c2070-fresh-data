# WS4 tiled 30-m dataset — H20|ON|S23

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `H20|ON|S23` (parent `H20|ON`)
- Tile / row / col: `H20` / 2 / 3
- Province: `ON`
- Centroid: 55.115914, -85.169628
- Allocated harvest: 5639.640098 m3
- Productive subcell area: 99397.260038 ha
- Committed geometry area: 220363.210607 ha
- Clipped inventory geometry: 220363.210607 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1080137
- Blocks: 519671
- Forest area: 97212.33 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 44706
- Scheduled area: 8155.26 ha
- Eligible blocks (age class >= 40): 447059
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 15.00 MB
- Schedules: 0.53 MB
- Runs: 0.00 MB
- Total: 15.53 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
