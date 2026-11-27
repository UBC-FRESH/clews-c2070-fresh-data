# WS4 tiled 30-m dataset — J15|MB|S32

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `J15|MB|S32` (parent `J15|MB`)
- Tile / row / col: `J15` / 3 / 2
- Province: `MB`
- Centroid: 58.750003, -98.299637
- Allocated harvest: 3228.639423 m3
- Productive subcell area: 155253.293299 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1257968
- Blocks: 419902
- Forest area: 113217.12 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 31100
- Scheduled area: 7726.86 ha
- Eligible blocks (age class >= 40): 310994
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 15.06 MB
- Schedules: 0.37 MB
- Runs: 0.00 MB
- Total: 15.43 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
