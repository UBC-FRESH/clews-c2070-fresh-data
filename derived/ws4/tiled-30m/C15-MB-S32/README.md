# WS4 tiled 30-m dataset — C15|MB|S32

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `C15|MB|S32` (parent `C15|MB`)
- Tile / row / col: `C15` / 3 / 2
- Province: `MB`
- Centroid: 49.202537, -97.551239
- Allocated harvest: 1527.904535 m3
- Productive subcell area: 36286.315009 ha
- Committed geometry area: 224035.617604 ha
- Clipped inventory geometry: 224035.617604 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 131378
- Blocks: 50464
- Forest area: 11824.02 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 1309
- Scheduled area: 274.77 ha
- Eligible blocks (age class >= 40): 13087
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 2.06 MB
- Schedules: 0.01 MB
- Runs: 0.00 MB
- Total: 2.07 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
