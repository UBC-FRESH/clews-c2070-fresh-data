# WS4 tiled 30-m dataset — E23|QC|S23

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `E23|QC|S23` (parent `E23|QC`)
- Tile / row / col: `E23` / 2 / 3
- Province: `QC`
- Centroid: 50.401108, -79.483620
- Allocated harvest: 1608.648542 m3
- Productive subcell area: 6860.881130 ha
- Committed geometry area: 11260.743901 ha
- Clipped inventory geometry: 11260.743901 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 85554
- Blocks: 34419
- Forest area: 7699.86 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 2903
- Scheduled area: 576.72 ha
- Eligible blocks (age class >= 40): 29024
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 1.43 MB
- Schedules: 0.03 MB
- Runs: 0.00 MB
- Total: 1.46 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
