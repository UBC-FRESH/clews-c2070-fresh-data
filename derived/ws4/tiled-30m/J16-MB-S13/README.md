# WS4 tiled 30-m dataset — J16|MB|S13

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `J16|MB|S13` (parent `J16|MB`)
- Tile / row / col: `J16` / 1 / 3
- Province: `MB`
- Centroid: 57.872784, -94.756510
- Allocated harvest: 1129.821957 m3
- Productive subcell area: 82327.066320 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1209360
- Blocks: 501879
- Forest area: 108842.40 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 41734
- Scheduled area: 8704.98 ha
- Eligible blocks (age class >= 40): 417333
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 15.86 MB
- Schedules: 0.49 MB
- Runs: 0.00 MB
- Total: 16.35 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
