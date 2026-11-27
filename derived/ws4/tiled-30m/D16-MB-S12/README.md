# WS4 tiled 30-m dataset — D16|MB|S12

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `D16|MB|S12` (parent `D16|MB`)
- Tile / row / col: `D16` / 1 / 2
- Province: `MB`
- Centroid: 49.662248, -95.501724
- Allocated harvest: 9151.081425 m3
- Productive subcell area: 174663.710049 ha
- Committed geometry area: 247686.211449 ha
- Clipped inventory geometry: 247686.211449 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2256743
- Blocks: 1008718
- Forest area: 203106.87 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 96474
- Scheduled area: 19218.96 ha
- Eligible blocks (age class >= 40): 964738
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 30.40 MB
- Schedules: 1.15 MB
- Runs: 0.00 MB
- Total: 31.55 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
