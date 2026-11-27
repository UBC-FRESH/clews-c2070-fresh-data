# WS4 tiled 30-m dataset — L8|AB|S21

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `L8|AB|S21` (parent `L8|AB`)
- Tile / row / col: `L8` / 2 / 1
- Province: `AB`
- Centroid: 58.890157, -118.436631
- Allocated harvest: 105518.724816 m3
- Productive subcell area: 196148.635131 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1953501
- Blocks: 957597
- Forest area: 175815.09 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 89044
- Scheduled area: 15354.09 ha
- Eligible blocks (age class >= 40): 890438
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 27.02 MB
- Schedules: 1.06 MB
- Runs: 0.00 MB
- Total: 28.07 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
