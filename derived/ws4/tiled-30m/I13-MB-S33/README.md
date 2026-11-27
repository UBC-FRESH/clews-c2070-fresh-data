# WS4 tiled 30-m dataset — I13|MB|S33

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `I13|MB|S33` (parent `I13|MB`)
- Tile / row / col: `I13` / 3 / 3
- Province: `MB`
- Centroid: 57.094691, -101.981280
- Allocated harvest: 205.756409 m3
- Productive subcell area: 6609.747535 ha
- Committed geometry area: 8888.342491 ha
- Clipped inventory geometry: 8888.342491 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 39205
- Blocks: 5905
- Forest area: 3528.45 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 3289
- Scheduled area: 709.47 ha
- Eligible blocks (age class >= 40): 3289
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 0.47 MB
- Schedules: 0.03 MB
- Runs: 0.00 MB
- Total: 0.50 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
