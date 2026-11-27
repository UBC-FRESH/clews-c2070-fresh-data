# WS4 tiled 30-m dataset — P2|YT|S23

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `P2|YT|S23` (parent `P2|YT`)
- Tile / row / col: `P2` / 2 / 3
- Province: `YT`
- Centroid: 60.171870, -136.490097
- Allocated harvest: 132.467364 m3
- Productive subcell area: 57592.236839 ha
- Committed geometry area: 202971.431453 ha
- Clipped inventory geometry: 202971.431453 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 556778
- Blocks: 365366
- Forest area: 50110.02 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 32981
- Scheduled area: 4432.68 ha
- Eligible blocks (age class >= 40): 329804
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 9.53 MB
- Schedules: 0.39 MB
- Runs: 0.00 MB
- Total: 9.92 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
