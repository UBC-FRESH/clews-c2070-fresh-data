# WS4 tiled 30-m dataset — S8|NT|S12

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `S8|NT|S12` (parent `S8|NT`)
- Tile / row / col: `S8` / 1 / 2
- Province: `NT`
- Centroid: 67.507566, -126.014574
- Allocated harvest: 79.975941 m3
- Productive subcell area: 197187.654852 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1716631
- Blocks: 604454
- Forest area: 154496.79 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 53155
- Scheduled area: 13375.62 ha
- Eligible blocks (age class >= 40): 531545
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 20.56 MB
- Schedules: 0.63 MB
- Runs: 0.00 MB
- Total: 21.19 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
