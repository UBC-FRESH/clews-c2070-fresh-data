# WS4 tiled 30-m dataset — G17|ON|S22

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `G17|ON|S22` (parent `G17|ON`)
- Tile / row / col: `G17` / 2 / 2
- Province: `ON`
- Centroid: 54.084585, -93.004647
- Allocated harvest: 7784.549654 m3
- Productive subcell area: 53502.395365 ha
- Committed geometry area: 67776.229333 ha
- Clipped inventory geometry: 67776.229333 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 558932
- Blocks: 193057
- Forest area: 50303.88 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 16777
- Scheduled area: 3236.40 ha
- Eligible blocks (age class >= 40): 167761
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 7.27 MB
- Schedules: 0.19 MB
- Runs: 0.00 MB
- Total: 7.46 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
