# WS4 tiled 30-m dataset — I2|BC|S21

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `I2|BC|S21` (parent `I2|BC`)
- Tile / row / col: `I2` / 2 / 1
- Province: `BC`
- Centroid: 51.606075, -128.044374
- Allocated harvest: 17355.308317 m3
- Productive subcell area: 23587.961411 ha
- Committed geometry area: 34767.985314 ha
- Clipped inventory geometry: 34767.985314 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 366990
- Blocks: 176627
- Forest area: 33029.10 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 17516
- Scheduled area: 3318.75 ha
- Eligible blocks (age class >= 40): 175157
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 5.81 MB
- Schedules: 0.20 MB
- Runs: 0.00 MB
- Total: 6.01 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
