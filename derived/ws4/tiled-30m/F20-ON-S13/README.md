# WS4 tiled 30-m dataset — F20|ON|S13

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `F20|ON|S13` (parent `F20|ON`)
- Tile / row / col: `F20` / 1 / 3
- Province: `ON`
- Centroid: 51.981173, -85.936827
- Allocated harvest: 18948.717397 m3
- Productive subcell area: 159984.952731 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1359510
- Blocks: 615366
- Forest area: 122355.90 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 57491
- Scheduled area: 11773.62 ha
- Eligible blocks (age class >= 40): 574906
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 18.76 MB
- Schedules: 0.68 MB
- Runs: 0.00 MB
- Total: 19.44 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
