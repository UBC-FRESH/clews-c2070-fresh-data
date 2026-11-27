# WS4 tiled 30-m dataset — E15|MB|S13

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `E15|MB|S13` (parent `E15|MB`)
- Tile / row / col: `E15` / 1 / 3
- Province: `MB`
- Centroid: 50.999388, -96.950566
- Allocated harvest: 4595.511204 m3
- Productive subcell area: 108701.166960 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 640012
- Blocks: 254437
- Forest area: 57601.08 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 21771
- Scheduled area: 5357.52 ha
- Eligible blocks (age class >= 40): 217701
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 8.65 MB
- Schedules: 0.25 MB
- Runs: 0.00 MB
- Total: 8.91 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
