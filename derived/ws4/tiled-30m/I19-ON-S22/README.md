# WS4 tiled 30-m dataset — I19|ON|S22

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `I19|ON|S22` (parent `I19|ON`)
- Tile / row / col: `I19` / 2 / 2
- Province: `ON`
- Centroid: 56.569220, -88.423531
- Allocated harvest: 189.746811 m3
- Productive subcell area: 3618.578601 ha
- Committed geometry area: 8837.223325 ha
- Clipped inventory geometry: 8837.223325 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 16663
- Blocks: 5985
- Forest area: 1499.67 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 4320
- Scheduled area: 1150.65 ha
- Eligible blocks (age class >= 40): 4320
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 0.31 MB
- Schedules: 0.04 MB
- Runs: 0.00 MB
- Total: 0.35 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
