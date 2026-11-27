# WS4 tiled 30-m dataset — F22|ON|S23

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `F22|ON|S23` (parent `F22|ON`)
- Tile / row / col: `F22` / 2 / 3
- Province: `ON`
- Centroid: 51.932322, -81.487608
- Allocated harvest: 7980.110381 m3
- Productive subcell area: 120279.541604 ha
- Committed geometry area: 229494.287546 ha
- Clipped inventory geometry: 229494.287546 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1038019
- Blocks: 525171
- Forest area: 93421.71 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 45922
- Scheduled area: 8443.98 ha
- Eligible blocks (age class >= 40): 459217
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 14.77 MB
- Schedules: 0.54 MB
- Runs: 0.00 MB
- Total: 15.31 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
