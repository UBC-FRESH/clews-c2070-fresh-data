# WS4 tiled 30-m dataset — K16|MB|S12

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `K16|MB|S12` (parent `K16|MB`)
- Tile / row / col: `K16` / 1 / 2
- Province: `MB`
- Centroid: 59.253961, -95.646943
- Allocated harvest: 777.549872 m3
- Productive subcell area: 42042.920874 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 208829
- Blocks: 118655
- Forest area: 18794.61 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 7054
- Scheduled area: 1183.50 ha
- Eligible blocks (age class >= 40): 70540
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 3.96 MB
- Schedules: 0.08 MB
- Runs: 0.00 MB
- Total: 4.04 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
