# WS4 tiled 30-m dataset — E30|NB|S11

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `E30|NB|S11` (parent `E30|NB`)
- Tile / row / col: `E30` / 1 / 1
- Province: `NB`
- Centroid: 47.137898, -67.744733
- Allocated harvest: 140885.426359 m3
- Productive subcell area: 133287.037558 ha
- Committed geometry area: 140514.356263 ha
- Clipped inventory geometry: 140514.356263 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1164813
- Blocks: 462887
- Forest area: 104833.17 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 35200
- Scheduled area: 6461.82 ha
- Eligible blocks (age class >= 40): 351993
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 15.27 MB
- Schedules: 0.41 MB
- Runs: 0.00 MB
- Total: 15.69 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
