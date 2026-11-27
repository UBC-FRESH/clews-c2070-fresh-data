# WS4 tiled 30-m dataset — D31|NB|S13

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `D31|NB|S13` (parent `D31|NB`)
- Tile / row / col: `D31` / 1 / 3
- Province: `NB`
- Centroid: 45.212855, -65.914672
- Allocated harvest: 1170.600522 m3
- Productive subcell area: 1305.053887 ha
- Committed geometry area: 1492.538408 ha
- Clipped inventory geometry: 1492.538408 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 14906
- Blocks: 6095
- Forest area: 1341.54 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 535
- Scheduled area: 109.08 ha
- Eligible blocks (age class >= 40): 5345
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 0.30 MB
- Schedules: 0.01 MB
- Runs: 0.00 MB
- Total: 0.31 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
