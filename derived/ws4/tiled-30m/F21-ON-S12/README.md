# WS4 tiled 30-m dataset — F21|ON|S12

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `F21|ON|S12` (parent `F21|ON`)
- Tile / row / col: `F21` / 1 / 2
- Province: `ON`
- Centroid: 51.841968, -84.485869
- Allocated harvest: 9105.239574 m3
- Productive subcell area: 122428.732512 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1421749
- Blocks: 485541
- Forest area: 127957.41 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 44264
- Scheduled area: 12424.59 ha
- Eligible blocks (age class >= 40): 442633
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 17.42 MB
- Schedules: 0.52 MB
- Runs: 0.00 MB
- Total: 17.94 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
