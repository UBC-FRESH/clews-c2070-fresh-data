# WS4 tiled 30-m dataset — B22|ON|S12

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `B22|ON|S12` (parent `B22|ON`)
- Tile / row / col: `B22` / 1 / 2
- Province: `ON`
- Centroid: 46.357843, -83.842095
- Allocated harvest: 40493.312880 m3
- Productive subcell area: 138233.968509 ha
- Committed geometry area: 153570.808388 ha
- Clipped inventory geometry: 153570.808388 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1370997
- Blocks: 414570
- Forest area: 123389.73 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 37959
- Scheduled area: 11768.67 ha
- Eligible blocks (age class >= 40): 379585
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 16.27 MB
- Schedules: 0.45 MB
- Runs: 0.00 MB
- Total: 16.72 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
