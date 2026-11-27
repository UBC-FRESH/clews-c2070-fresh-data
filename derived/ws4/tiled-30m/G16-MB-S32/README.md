# WS4 tiled 30-m dataset — G16|MB|S32

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `G16|MB|S32` (parent `G16|MB`)
- Tile / row / col: `G16` / 3 / 2
- Province: `MB`
- Centroid: 54.658485, -95.566692
- Allocated harvest: 7060.965475 m3
- Productive subcell area: 187107.934041 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1862774
- Blocks: 722732
- Forest area: 167649.66 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 67166
- Scheduled area: 13956.39 ha
- Eligible blocks (age class >= 40): 671659
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 23.21 MB
- Schedules: 0.80 MB
- Runs: 0.00 MB
- Total: 24.00 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
