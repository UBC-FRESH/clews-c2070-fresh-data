# WS4 tiled 30-m dataset — E15|MB|S23

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `E15|MB|S23` (parent `E15|MB`)
- Tile / row / col: `E15` / 2 / 3
- Province: `MB`
- Centroid: 51.452237, -96.972815
- Allocated harvest: 4595.511204 m3
- Productive subcell area: 108701.166960 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1357254
- Blocks: 546244
- Forest area: 122152.86 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 51556
- Scheduled area: 11406.69 ha
- Eligible blocks (age class >= 40): 515556
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 17.79 MB
- Schedules: 0.61 MB
- Runs: 0.00 MB
- Total: 18.40 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
