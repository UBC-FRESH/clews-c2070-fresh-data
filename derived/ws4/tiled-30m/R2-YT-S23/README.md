# WS4 tiled 30-m dataset — R2|YT|S23

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `R2|YT|S23` (parent `R2|YT`)
- Tile / row / col: `R2` / 2 / 3
- Province: `YT`
- Centroid: 62.283030, -140.112207
- Allocated harvest: 271.575405 m3
- Productive subcell area: 128839.581913 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1811726
- Blocks: 688238
- Forest area: 163055.34 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 55973
- Scheduled area: 11724.21 ha
- Eligible blocks (age class >= 40): 559722
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 22.41 MB
- Schedules: 0.66 MB
- Runs: 0.00 MB
- Total: 23.07 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
