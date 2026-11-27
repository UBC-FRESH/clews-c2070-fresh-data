# WS4 tiled 30-m dataset — F18|ON|S22

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `F18|ON|S22` (parent `F18|ON`)
- Tile / row / col: `F18` / 2 / 2
- Province: `ON`
- Centroid: 52.759450, -91.034550
- Allocated harvest: 34530.189706 m3
- Productive subcell area: 199564.008806 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2012746
- Blocks: 600506
- Forest area: 181147.14 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 55024
- Scheduled area: 13030.74 ha
- Eligible blocks (age class >= 40): 550234
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 22.54 MB
- Schedules: 0.65 MB
- Runs: 0.00 MB
- Total: 23.19 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
