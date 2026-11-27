# WS4 tiled 30-m dataset — E15|MB|S33

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `E15|MB|S33` (parent `E15|MB`)
- Tile / row / col: `E15` / 3 / 3
- Province: `MB`
- Centroid: 51.905728, -96.995579
- Allocated harvest: 4595.511204 m3
- Productive subcell area: 108701.166960 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 995030
- Blocks: 381019
- Forest area: 89552.70 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 36700
- Scheduled area: 8310.78 ha
- Eligible blocks (age class >= 40): 366999
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 12.73 MB
- Schedules: 0.43 MB
- Runs: 0.00 MB
- Total: 13.16 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
