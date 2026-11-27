# WS4 tiled 30-m dataset — J17|MB|S12

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `J17|MB|S12` (parent `J17|MB`)
- Tile / row / col: `J17` / 1 / 2
- Province: `MB`
- Centroid: 57.844149, -93.094909
- Allocated harvest: 617.879236 m3
- Productive subcell area: 46818.826443 ha
- Committed geometry area: 209963.136289 ha
- Clipped inventory geometry: 209963.136289 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 443744
- Blocks: 192187
- Forest area: 39936.96 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 13890
- Scheduled area: 3073.14 ha
- Eligible blocks (age class >= 40): 138895
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 6.42 MB
- Schedules: 0.16 MB
- Runs: 0.00 MB
- Total: 6.58 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
