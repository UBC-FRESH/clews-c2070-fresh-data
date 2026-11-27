# WS4 tiled 30-m dataset — G5|BC|S12

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `G5|BC|S12` (parent `G5|BC`)
- Tile / row / col: `G5` / 1 / 2
- Province: `BC`
- Centroid: 50.739373, -119.648643
- Allocated harvest: 139454.892072 m3
- Productive subcell area: 210408.981546 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2238490
- Blocks: 868997
- Forest area: 201464.10 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 73415
- Scheduled area: 12516.93 ha
- Eligible blocks (age class >= 40): 734147
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 28.13 MB
- Schedules: 0.87 MB
- Runs: 0.00 MB
- Total: 29.00 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
