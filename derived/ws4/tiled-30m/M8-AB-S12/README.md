# WS4 tiled 30-m dataset — M8|AB|S12

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `M8|AB|S12` (parent `M8|AB`)
- Tile / row / col: `M8` / 1 / 2
- Province: `AB`
- Centroid: 59.847238, -118.233400
- Allocated harvest: 31725.429109 m3
- Productive subcell area: 83842.084337 ha
- Committed geometry area: 173460.427313 ha
- Clipped inventory geometry: 173460.427313 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 818376
- Blocks: 250940
- Forest area: 73653.84 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 17015
- Scheduled area: 4205.61 ha
- Eligible blocks (age class >= 40): 170147
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 9.56 MB
- Schedules: 0.20 MB
- Runs: 0.00 MB
- Total: 9.76 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
