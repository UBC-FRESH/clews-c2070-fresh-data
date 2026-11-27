# WS4 tiled 30-m dataset — H15|MB|S22

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `H15|MB|S22` (parent `H15|MB`)
- Tile / row / col: `H15` / 2 / 2
- Province: `MB`
- Centroid: 55.535518, -98.006275
- Allocated harvest: 7584.915428 m3
- Productive subcell area: 194721.647177 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2186375
- Blocks: 790793
- Forest area: 196773.75 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 74307
- Scheduled area: 17952.03 ha
- Eligible blocks (age class >= 40): 743061
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 26.96 MB
- Schedules: 0.88 MB
- Runs: 0.00 MB
- Total: 27.84 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
