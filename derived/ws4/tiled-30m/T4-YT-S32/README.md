# WS4 tiled 30-m dataset — T4|YT|S32

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `T4|YT|S32` (parent `T4|YT`)
- Tile / row / col: `T4` / 3 / 2
- Province: `YT`
- Centroid: 66.248754, -140.728587
- Allocated harvest: 87.785882 m3
- Productive subcell area: 69313.135562 ha
- Committed geometry area: 129995.988078 ha
- Clipped inventory geometry: 129995.988078 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1057602
- Blocks: 441730
- Forest area: 95184.18 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 37610
- Scheduled area: 7882.47 ha
- Eligible blocks (age class >= 40): 376096
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 13.91 MB
- Schedules: 0.44 MB
- Runs: 0.00 MB
- Total: 14.35 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
