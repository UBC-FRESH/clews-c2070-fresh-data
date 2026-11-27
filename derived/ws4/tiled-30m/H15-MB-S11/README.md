# WS4 tiled 30-m dataset — H15|MB|S11

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `H15|MB|S11` (parent `H15|MB`)
- Tile / row / col: `H15` / 1 / 1
- Province: `MB`
- Centroid: 55.053671, -98.765287
- Allocated harvest: 7584.915428 m3
- Productive subcell area: 194721.647177 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2296419
- Blocks: 830626
- Forest area: 206677.71 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 81194
- Scheduled area: 20289.42 ha
- Eligible blocks (age class >= 40): 811934
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 28.48 MB
- Schedules: 0.96 MB
- Runs: 0.00 MB
- Total: 29.45 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
