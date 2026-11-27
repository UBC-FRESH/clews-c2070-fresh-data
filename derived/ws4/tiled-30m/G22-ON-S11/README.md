# WS4 tiled 30-m dataset — G22|ON|S11

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `G22|ON|S11` (parent `G22|ON`)
- Tile / row / col: `G22` / 1 / 1
- Province: `ON`
- Centroid: 53.018369, -82.637968
- Allocated harvest: 8492.162663 m3
- Productive subcell area: 114747.501450 ha
- Committed geometry area: 240153.095885 ha
- Clipped inventory geometry: 240153.095885 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1564832
- Blocks: 583336
- Forest area: 140834.88 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 52709
- Scheduled area: 12558.78 ha
- Eligible blocks (age class >= 40): 527082
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 19.74 MB
- Schedules: 0.62 MB
- Runs: 0.00 MB
- Total: 20.36 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
