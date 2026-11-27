# WS4 tiled 30-m dataset — F22|ON|S21

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `F22|ON|S21` (parent `F22|ON`)
- Tile / row / col: `F22` / 2 / 1
- Province: `ON`
- Centroid: 52.128419, -82.907944
- Allocated harvest: 8693.147078 m3
- Productive subcell area: 131026.727169 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 945066
- Blocks: 386549
- Forest area: 85055.94 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 33876
- Scheduled area: 7646.22 ha
- Eligible blocks (age class >= 40): 338751
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 12.29 MB
- Schedules: 0.40 MB
- Runs: 0.00 MB
- Total: 12.69 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
