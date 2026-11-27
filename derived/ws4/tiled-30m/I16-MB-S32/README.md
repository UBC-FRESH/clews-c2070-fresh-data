# WS4 tiled 30-m dataset — I16|MB|S32

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `I16|MB|S32` (parent `I16|MB`)
- Tile / row / col: `I16` / 3 / 2
- Province: `MB`
- Centroid: 57.411220, -95.612262
- Allocated harvest: 3456.593616 m3
- Productive subcell area: 133820.004351 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1012868
- Blocks: 342199
- Forest area: 91158.12 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 23148
- Scheduled area: 5758.83 ha
- Eligible blocks (age class >= 40): 231479
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 12.11 MB
- Schedules: 0.27 MB
- Runs: 0.00 MB
- Total: 12.38 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
