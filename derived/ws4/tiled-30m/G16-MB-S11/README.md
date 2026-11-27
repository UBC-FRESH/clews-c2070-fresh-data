# WS4 tiled 30-m dataset — G16|MB|S11

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `G16|MB|S11` (parent `G16|MB`)
- Tile / row / col: `G16` / 1 / 1
- Province: `MB`
- Centroid: 53.737944, -96.322749
- Allocated harvest: 7060.965475 m3
- Productive subcell area: 187107.934041 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2008530
- Blocks: 621284
- Forest area: 180767.70 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 48886
- Scheduled area: 9146.34 ha
- Eligible blocks (age class >= 40): 488857
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 22.54 MB
- Schedules: 0.58 MB
- Runs: 0.00 MB
- Total: 23.12 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
