# WS4 tiled 30-m dataset — K15|MB|S33

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `K15|MB|S33` (parent `K15|MB`)
- Tile / row / col: `K15` / 3 / 3
- Province: `MB`
- Centroid: 59.961853, -97.521144
- Allocated harvest: 300.953500 m3
- Productive subcell area: 17503.542194 ha
- Committed geometry area: 42057.871809 ha
- Clipped inventory geometry: 42057.871809 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 24452
- Blocks: 14358
- Forest area: 2200.68 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 4446
- Scheduled area: 654.39 ha
- Eligible blocks (age class >= 40): 4446
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 0.53 MB
- Schedules: 0.05 MB
- Runs: 0.00 MB
- Total: 0.58 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
