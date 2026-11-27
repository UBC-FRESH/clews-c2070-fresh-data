# WS4 tiled 30-m dataset — K30|NL|S31

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `K30|NL|S31` (parent `K30|NL`)
- Tile / row / col: `K30` / 3 / 1
- Province: `NL`
- Centroid: 55.140104, -61.232388
- Allocated harvest: 10055.424619 m3
- Productive subcell area: 164665.481190 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1919197
- Blocks: 491709
- Forest area: 172727.73 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 39550
- Scheduled area: 13726.26 ha
- Eligible blocks (age class >= 40): 395492
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 20.19 MB
- Schedules: 0.47 MB
- Runs: 0.00 MB
- Total: 20.66 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
