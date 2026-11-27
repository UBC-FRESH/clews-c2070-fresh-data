# WS4 tiled 30-m dataset — F20|ON|S23

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `F20|ON|S23` (parent `F20|ON`)
- Tile / row / col: `F20` / 2 / 3
- Province: `ON`
- Centroid: 52.430951, -85.831180
- Allocated harvest: 18948.717397 m3
- Productive subcell area: 159984.952731 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 982691
- Blocks: 397796
- Forest area: 88442.19 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 36665
- Scheduled area: 8287.38 ha
- Eligible blocks (age class >= 40): 366646
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 12.83 MB
- Schedules: 0.43 MB
- Runs: 0.00 MB
- Total: 13.26 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
