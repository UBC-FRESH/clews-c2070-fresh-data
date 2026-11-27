# WS4 tiled 30-m dataset — S8|NT|S21

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `S8|NT|S21` (parent `S8|NT`)
- Tile / row / col: `S8` / 2 / 1
- Province: `NT`
- Centroid: 67.691055, -127.657054
- Allocated harvest: 79.975941 m3
- Productive subcell area: 197187.654852 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1836905
- Blocks: 790481
- Forest area: 165321.45 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 63990
- Scheduled area: 11260.98 ha
- Eligible blocks (age class >= 40): 639892
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 23.65 MB
- Schedules: 0.76 MB
- Runs: 0.00 MB
- Total: 24.41 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
