# WS4 tiled 30-m dataset — I18|ON|S23

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `I18|ON|S23` (parent `I18|ON`)
- Tile / row / col: `I18` / 2 / 3
- Province: `ON`
- Centroid: 56.602787, -89.368030
- Allocated harvest: 28.565615 m3
- Productive subcell area: 556.903108 ha
- Committed geometry area: 1181.205042 ha
- Clipped inventory geometry: 1181.205042 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 7237
- Blocks: 2694
- Forest area: 651.33 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 2142
- Scheduled area: 560.34 ha
- Eligible blocks (age class >= 40): 2142
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 0.17 MB
- Schedules: 0.02 MB
- Runs: 0.00 MB
- Total: 0.19 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
