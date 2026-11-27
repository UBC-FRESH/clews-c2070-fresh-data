# WS4 tiled 30-m dataset — G6|BC|S12

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `G6|BC|S12` (parent `G6|BC`)
- Tile / row / col: `G6` / 1 / 2
- Province: `BC`
- Centroid: 51.232789, -117.643826
- Allocated harvest: 104404.379749 m3
- Productive subcell area: 145787.906891 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1461311
- Blocks: 784368
- Forest area: 131517.99 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 72265
- Scheduled area: 11357.64 ha
- Eligible blocks (age class >= 40): 722641
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 21.16 MB
- Schedules: 0.86 MB
- Runs: 0.00 MB
- Total: 22.01 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
