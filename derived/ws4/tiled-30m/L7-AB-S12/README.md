# WS4 tiled 30-m dataset — L7|AB|S12

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `L7|AB|S12` (parent `L7|AB`)
- Tile / row / col: `L7` / 1 / 2
- Province: `AB`
- Centroid: 58.117905, -119.665340
- Allocated harvest: 97033.412622 m3
- Productive subcell area: 171857.778068 ha
- Committed geometry area: 203432.746732 ha
- Clipped inventory geometry: 203432.746732 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1993262
- Blocks: 672924
- Forest area: 179393.58 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 55446
- Scheduled area: 11325.51 ha
- Eligible blocks (age class >= 40): 554456
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 23.02 MB
- Schedules: 0.66 MB
- Runs: 0.00 MB
- Total: 23.68 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
