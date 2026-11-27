# WS4 tiled 30-m dataset — R6|NT|S32

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `R6|NT|S32` (parent `R6|NT`)
- Tile / row / col: `R6` / 3 / 2
- Province: `NT`
- Centroid: 65.705033, -131.445797
- Allocated harvest: 64.971190 m3
- Productive subcell area: 94649.713824 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2202256
- Blocks: 823095
- Forest area: 198203.04 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 65507
- Scheduled area: 15964.92 ha
- Eligible blocks (age class >= 40): 655063
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 27.21 MB
- Schedules: 0.78 MB
- Runs: 0.00 MB
- Total: 27.99 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
