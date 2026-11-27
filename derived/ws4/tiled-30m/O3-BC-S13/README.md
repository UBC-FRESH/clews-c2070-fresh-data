# WS4 tiled 30-m dataset — O3|BC|S13

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `O3|BC|S13` (parent `O3|BC`)
- Tile / row / col: `O3` / 1 / 3
- Province: `BC`
- Centroid: 59.424504, -132.132746
- Allocated harvest: 56414.204122 m3
- Productive subcell area: 138591.993275 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2285123
- Blocks: 1235928
- Forest area: 205661.07 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 119649
- Scheduled area: 19073.07 ha
- Eligible blocks (age class >= 40): 1196486
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 33.84 MB
- Schedules: 1.45 MB
- Runs: 0.00 MB
- Total: 35.29 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
