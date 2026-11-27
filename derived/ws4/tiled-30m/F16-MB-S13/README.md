# WS4 tiled 30-m dataset — F16|MB|S13

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `F16|MB|S13` (parent `F16|MB`)
- Tile / row / col: `F16` / 1 / 3
- Province: `MB`
- Centroid: 52.386659, -95.157630
- Allocated harvest: 91.640628 m3
- Productive subcell area: 2477.655509 ha
- Committed geometry area: 3034.685826 ha
- Clipped inventory geometry: 3034.685826 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 27378
- Blocks: 5686
- Forest area: 2464.02 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 3639
- Scheduled area: 1282.05 ha
- Eligible blocks (age class >= 40): 3639
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 0.39 MB
- Schedules: 0.04 MB
- Runs: 0.00 MB
- Total: 0.42 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
