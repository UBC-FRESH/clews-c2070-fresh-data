# WS4 tiled 30-m dataset — O6|NT|S13

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `O6|NT|S13` (parent `O6|NT`)
- Tile / row / col: `O6` / 1 / 3
- Province: `NT`
- Centroid: 61.517028, -124.848331
- Allocated harvest: 101.797925 m3
- Productive subcell area: 122838.100117 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1387445
- Blocks: 684150
- Forest area: 124870.05 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 57988
- Scheduled area: 11084.13 ha
- Eligible blocks (age class >= 40): 579871
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 19.71 MB
- Schedules: 0.69 MB
- Runs: 0.00 MB
- Total: 20.40 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
