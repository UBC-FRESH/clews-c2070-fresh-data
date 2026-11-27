# WS4 tiled 30-m dataset — I17|MB|S23

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `I17|MB|S23` (parent `I17|MB`)
- Tile / row / col: `I17` / 2 / 3
- Province: `MB`
- Centroid: 56.877379, -92.239558
- Allocated harvest: 1364.891634 m3
- Productive subcell area: 99228.650491 ha
- Committed geometry area: 199596.626301 ha
- Clipped inventory geometry: 199596.626301 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1228846
- Blocks: 570710
- Forest area: 110596.14 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 49727
- Scheduled area: 9827.55 ha
- Eligible blocks (age class >= 40): 497262
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 16.96 MB
- Schedules: 0.59 MB
- Runs: 0.00 MB
- Total: 17.54 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
