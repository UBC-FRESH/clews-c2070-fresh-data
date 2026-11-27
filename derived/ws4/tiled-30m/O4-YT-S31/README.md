# WS4 tiled 30-m dataset — O4|YT|S31

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `O4|YT|S31` (parent `O4|YT`)
- Tile / row / col: `O4` / 3 / 1
- Province: `YT`
- Centroid: 60.449143, -132.383341
- Allocated harvest: 303.516384 m3
- Productive subcell area: 186577.766324 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2302571
- Blocks: 1064348
- Forest area: 207231.39 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 100223
- Scheduled area: 20079.81 ha
- Eligible blocks (age class >= 40): 1002226
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 31.51 MB
- Schedules: 1.20 MB
- Runs: 0.00 MB
- Total: 32.71 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
