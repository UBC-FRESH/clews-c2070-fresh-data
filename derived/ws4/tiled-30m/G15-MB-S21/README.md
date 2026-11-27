# WS4 tiled 30-m dataset — G15|MB|S21

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `G15|MB|S21` (parent `G15|MB`)
- Tile / row / col: `G15` / 2 / 1
- Province: `MB`
- Centroid: 54.140499, -98.673220
- Allocated harvest: 5714.956909 m3
- Productive subcell area: 162277.652207 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1784885
- Blocks: 668433
- Forest area: 160639.65 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 64003
- Scheduled area: 15176.97 ha
- Eligible blocks (age class >= 40): 640023
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 22.41 MB
- Schedules: 0.76 MB
- Runs: 0.00 MB
- Total: 23.16 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
