# WS4 tiled 30-m dataset — H36|NL|S32

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `H36|NL|S32` (parent `H36|NL`)
- Tile / row / col: `H36` / 3 / 2
- Province: `NL`
- Centroid: 46.954013, -53.446297
- Allocated harvest: 7920.736256 m3
- Productive subcell area: 99065.993637 ha
- Committed geometry area: 184530.550143 ha
- Clipped inventory geometry: 184530.550143 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1069963
- Blocks: 545389
- Forest area: 96296.67 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 47310
- Scheduled area: 8696.16 ha
- Eligible blocks (age class >= 40): 473100
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 15.21 MB
- Schedules: 0.56 MB
- Runs: 0.00 MB
- Total: 15.76 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
