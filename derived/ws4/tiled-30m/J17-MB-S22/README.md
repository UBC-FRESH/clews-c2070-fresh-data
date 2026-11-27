# WS4 tiled 30-m dataset — J17|MB|S22

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `J17|MB|S22` (parent `J17|MB`)
- Tile / row / col: `J17` / 2 / 2
- Province: `MB`
- Centroid: 58.289678, -93.207489
- Allocated harvest: 372.761139 m3
- Productive subcell area: 28245.388518 ha
- Committed geometry area: 126668.923796 ha
- Clipped inventory geometry: 126668.923796 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 66896
- Blocks: 36944
- Forest area: 6020.64 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 2328
- Scheduled area: 415.26 ha
- Eligible blocks (age class >= 40): 23278
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 1.30 MB
- Schedules: 0.02 MB
- Runs: 0.00 MB
- Total: 1.33 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
