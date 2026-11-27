# WS4 tiled 30-m dataset — I15|MB|S33

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `I15|MB|S33` (parent `I15|MB`)
- Tile / row / col: `I15` / 3 / 3
- Province: `MB`
- Centroid: 57.390040, -97.316274
- Allocated harvest: 5439.614180 m3
- Productive subcell area: 170601.009204 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1766293
- Blocks: 488498
- Forest area: 158966.37 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 36829
- Scheduled area: 14840.37 ha
- Eligible blocks (age class >= 40): 368282
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 19.21 MB
- Schedules: 0.44 MB
- Runs: 0.00 MB
- Total: 19.64 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
