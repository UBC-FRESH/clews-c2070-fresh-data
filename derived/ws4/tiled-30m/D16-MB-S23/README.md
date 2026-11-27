# WS4 tiled 30-m dataset — D16|MB|S23

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `D16|MB|S23` (parent `D16|MB`)
- Tile / row / col: `D16` / 2 / 3
- Province: `MB`
- Centroid: 50.201693, -95.153251
- Allocated harvest: 4.562846 m3
- Productive subcell area: 87.089547 ha
- Committed geometry area: 123.499495 ha
- Clipped inventory geometry: 123.499495 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1136
- Blocks: 801
- Forest area: 102.24 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 777
- Scheduled area: 99.36 ha
- Eligible blocks (age class >= 40): 777
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 0.10 MB
- Schedules: 0.01 MB
- Runs: 0.00 MB
- Total: 0.10 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
