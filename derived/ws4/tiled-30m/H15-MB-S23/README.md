# WS4 tiled 30-m dataset — H15|MB|S23

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `H15|MB|S23` (parent `H15|MB`)
- Tile / row / col: `H15` / 2 / 3
- Province: `MB`
- Centroid: 55.554267, -97.198509
- Allocated harvest: 7584.915428 m3
- Productive subcell area: 194721.647177 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2176308
- Blocks: 680031
- Forest area: 195867.72 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 61577
- Scheduled area: 15429.87 ha
- Eligible blocks (age class >= 40): 615769
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 25.09 MB
- Schedules: 0.73 MB
- Runs: 0.00 MB
- Total: 25.82 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
