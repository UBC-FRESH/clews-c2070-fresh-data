# WS4 tiled 30-m dataset — C16|MB|S32

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `C16|MB|S32` (parent `C16|MB`)
- Tile / row / col: `C16` / 3 / 2
- Province: `MB`
- Centroid: 49.227224, -95.514526
- Allocated harvest: 9178.572399 m3
- Productive subcell area: 171677.468914 ha
- Committed geometry area: 225343.834117 ha
- Clipped inventory geometry: 225343.834117 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2021545
- Blocks: 702495
- Forest area: 181939.05 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 66334
- Scheduled area: 16551.36 ha
- Eligible blocks (age class >= 40): 663332
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 24.51 MB
- Schedules: 0.79 MB
- Runs: 0.00 MB
- Total: 25.29 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
