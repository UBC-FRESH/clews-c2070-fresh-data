# WS4 tiled 30-m dataset — H11|SK|S23

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `H11|SK|S23` (parent `H11|SK`)
- Tile / row / col: `H11` / 2 / 3
- Province: `SK`
- Centroid: 54.950078, -106.772644
- Allocated harvest: 45593.936486 m3
- Productive subcell area: 190474.751403 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1637486
- Blocks: 558452
- Forest area: 147373.74 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 44653
- Scheduled area: 8557.29 ha
- Eligible blocks (age class >= 40): 446530
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 19.32 MB
- Schedules: 0.53 MB
- Runs: 0.00 MB
- Total: 19.85 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
