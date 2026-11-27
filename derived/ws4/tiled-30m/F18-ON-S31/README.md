# WS4 tiled 30-m dataset — F18|ON|S31

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `F18|ON|S31` (parent `F18|ON`)
- Tile / row / col: `F18` / 3 / 1
- Province: `ON`
- Centroid: 53.240037, -91.745501
- Allocated harvest: 34530.189706 m3
- Productive subcell area: 199564.008806 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2277757
- Blocks: 693219
- Forest area: 204998.13 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 66419
- Scheduled area: 19243.80 ha
- Eligible blocks (age class >= 40): 664182
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 26.17 MB
- Schedules: 0.79 MB
- Runs: 0.00 MB
- Total: 26.96 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
