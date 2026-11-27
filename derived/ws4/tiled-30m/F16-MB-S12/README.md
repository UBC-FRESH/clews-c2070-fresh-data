# WS4 tiled 30-m dataset — F16|MB|S12

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `F16|MB|S12` (parent `F16|MB`)
- Tile / row / col: `F16` / 1 / 2
- Province: `MB`
- Centroid: 52.378084, -95.533597
- Allocated harvest: 7549.432927 m3
- Productive subcell area: 204111.368633 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2169525
- Blocks: 537258
- Forest area: 195257.25 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 35425
- Scheduled area: 6876.99 ha
- Eligible blocks (age class >= 40): 354244
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 22.26 MB
- Schedules: 0.42 MB
- Runs: 0.00 MB
- Total: 22.67 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
