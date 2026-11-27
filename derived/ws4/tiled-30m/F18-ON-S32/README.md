# WS4 tiled 30-m dataset — F18|ON|S32

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `F18|ON|S32` (parent `F18|ON`)
- Tile / row / col: `F18` / 3 / 2
- Province: `ON`
- Centroid: 53.214014, -90.987247
- Allocated harvest: 34530.189706 m3
- Productive subcell area: 199564.008806 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2217752
- Blocks: 563626
- Forest area: 199597.68 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 49859
- Scheduled area: 16800.39 ha
- Eligible blocks (age class >= 40): 498585
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 23.28 MB
- Schedules: 0.59 MB
- Runs: 0.00 MB
- Total: 23.87 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
