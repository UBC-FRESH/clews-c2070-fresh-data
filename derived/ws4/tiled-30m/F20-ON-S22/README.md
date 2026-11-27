# WS4 tiled 30-m dataset — F20|ON|S22

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `F20|ON|S22` (parent `F20|ON`)
- Tile / row / col: `F20` / 2 / 2
- Province: `ON`
- Centroid: 52.493672, -86.568625
- Allocated harvest: 18948.717397 m3
- Productive subcell area: 159984.952731 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1755992
- Blocks: 747419
- Forest area: 158039.28 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 71097
- Scheduled area: 15002.37 ha
- Eligible blocks (age class >= 40): 710962
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 23.05 MB
- Schedules: 0.84 MB
- Runs: 0.00 MB
- Total: 23.89 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
