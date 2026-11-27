# WS4 tiled 30-m dataset — G20|ON|S12

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `G20|ON|S12` (parent `G20|ON`)
- Tile / row / col: `G20` / 1 / 2
- Province: `ON`
- Centroid: 53.396298, -86.366971
- Allocated harvest: 10027.306091 m3
- Productive subcell area: 122222.059994 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 882443
- Blocks: 538847
- Forest area: 79419.87 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 50750
- Scheduled area: 7552.71 ha
- Eligible blocks (age class >= 40): 507491
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 13.78 MB
- Schedules: 0.60 MB
- Runs: 0.00 MB
- Total: 14.38 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
