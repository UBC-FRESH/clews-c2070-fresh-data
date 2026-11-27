# WS4 tiled 30-m dataset — G5|BC|S13

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `G5|BC|S13` (parent `G5|BC`)
- Tile / row / col: `G5` / 1 / 3
- Province: `BC`
- Centroid: 50.908178, -118.985860
- Allocated harvest: 139454.892072 m3
- Productive subcell area: 210408.981546 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2270312
- Blocks: 937043
- Forest area: 204328.08 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 85935
- Scheduled area: 15591.06 ha
- Eligible blocks (age class >= 40): 859348
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 29.02 MB
- Schedules: 1.02 MB
- Runs: 0.00 MB
- Total: 30.04 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
