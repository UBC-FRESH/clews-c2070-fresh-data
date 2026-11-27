# WS4 tiled 30-m dataset — G17|ON|S11

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `G17|ON|S11` (parent `G17|ON`)
- Tile / row / col: `G17` / 1 / 1
- Province: `ON`
- Centroid: 53.591352, -93.763917
- Allocated harvest: 3875.378573 m3
- Productive subcell area: 26635.071499 ha
- Committed geometry area: 33741.007330 ha
- Clipped inventory geometry: 33741.007330 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 275127
- Blocks: 85295
- Forest area: 24761.43 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 6656
- Scheduled area: 1163.34 ha
- Eligible blocks (age class >= 40): 66559
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 3.61 MB
- Schedules: 0.07 MB
- Runs: 0.00 MB
- Total: 3.68 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
