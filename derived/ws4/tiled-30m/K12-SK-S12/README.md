# WS4 tiled 30-m dataset — K12|SK|S12

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `K12|SK|S12` (parent `K12|SK`)
- Tile / row / col: `K12` / 1 / 2
- Province: `SK`
- Centroid: 58.731665, -106.335057
- Allocated harvest: 15924.546966 m3
- Productive subcell area: 142937.039976 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1807377
- Blocks: 306268
- Forest area: 162663.93 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 15868
- Scheduled area: 19961.82 ha
- Eligible blocks (age class >= 40): 158679
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 16.06 MB
- Schedules: 0.18 MB
- Runs: 0.00 MB
- Total: 16.24 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
