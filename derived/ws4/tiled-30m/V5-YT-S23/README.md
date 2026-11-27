# WS4 tiled 30-m dataset — V5|YT|S23

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `V5|YT|S23` (parent `V5|YT`)
- Tile / row / col: `V5` / 2 / 3
- Province: `YT`
- Centroid: 69.191369, -140.835601
- Allocated harvest: 5.896796 m3
- Productive subcell area: 6013.426813 ha
- Committed geometry area: 44016.598900 ha
- Clipped inventory geometry: 44016.598900 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 9171
- Blocks: 6064
- Forest area: 825.39 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 1168
- Scheduled area: 153.27 ha
- Eligible blocks (age class >= 40): 1168
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 0.24 MB
- Schedules: 0.01 MB
- Runs: 0.00 MB
- Total: 0.25 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
