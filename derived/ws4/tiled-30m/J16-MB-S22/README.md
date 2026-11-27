# WS4 tiled 30-m dataset — J16|MB|S22

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `J16|MB|S22` (parent `J16|MB`)
- Tile / row / col: `J16` / 2 / 2
- Province: `MB`
- Centroid: 58.331959, -95.629125
- Allocated harvest: 1129.821957 m3
- Productive subcell area: 82327.066320 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 817074
- Blocks: 427759
- Forest area: 73536.66 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 31520
- Scheduled area: 5498.28 ha
- Eligible blocks (age class >= 40): 315196
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 11.93 MB
- Schedules: 0.37 MB
- Runs: 0.00 MB
- Total: 12.30 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
