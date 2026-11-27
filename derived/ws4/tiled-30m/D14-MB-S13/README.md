# WS4 tiled 30-m dataset — D14|MB|S13

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `D14|MB|S13` (parent `D14|MB`)
- Tile / row / col: `D14` / 1 / 3
- Province: `MB`
- Centroid: 49.582707, -98.965068
- Allocated harvest: 1077.408846 m3
- Productive subcell area: 23255.748089 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 692644
- Blocks: 153772
- Forest area: 62337.96 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 11568
- Scheduled area: 4681.08 ha
- Eligible blocks (age class >= 40): 115680
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 7.41 MB
- Schedules: 0.13 MB
- Runs: 0.00 MB
- Total: 7.54 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
