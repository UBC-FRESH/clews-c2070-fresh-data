# WS4 tiled 30-m dataset — P7|NT|S11

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `P7|NT|S11` (parent `P7|NT`)
- Tile / row / col: `P7` / 1 / 1
- Province: `NT`
- Centroid: 62.962831, -125.320697
- Allocated harvest: 136.701997 m3
- Productive subcell area: 163584.010344 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1396843
- Blocks: 606597
- Forest area: 125715.87 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 48148
- Scheduled area: 8860.14 ha
- Eligible blocks (age class >= 40): 481471
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 18.66 MB
- Schedules: 0.57 MB
- Runs: 0.00 MB
- Total: 19.23 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
