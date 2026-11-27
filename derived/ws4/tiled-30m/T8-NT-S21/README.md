# WS4 tiled 30-m dataset — T8|NT|S21

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `T8|NT|S21` (parent `T8|NT`)
- Tile / row / col: `T8` / 2 / 1
- Province: `NT`
- Centroid: 68.886161, -129.540444
- Allocated harvest: 5.324897 m3
- Productive subcell area: 11779.760064 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1393247
- Blocks: 622105
- Forest area: 125392.23 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 46912
- Scheduled area: 9471.42 ha
- Eligible blocks (age class >= 40): 469114
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 18.77 MB
- Schedules: 0.56 MB
- Runs: 0.00 MB
- Total: 19.33 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
