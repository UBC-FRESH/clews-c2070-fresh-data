# WS4 tiled 30-m dataset — F13|MB|S23

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `F13|MB|S23` (parent `F13|MB`)
- Tile / row / col: `F13` / 2 / 3
- Province: `MB`
- Centroid: 52.636090, -101.404904
- Allocated harvest: 6453.198628 m3
- Productive subcell area: 127868.215353 ha
- Committed geometry area: 165486.840754 ha
- Clipped inventory geometry: 165486.840754 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1672640
- Blocks: 472930
- Forest area: 150537.60 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 43334
- Scheduled area: 12931.92 ha
- Eligible blocks (age class >= 40): 433334
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 18.58 MB
- Schedules: 0.51 MB
- Runs: 0.00 MB
- Total: 19.09 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
