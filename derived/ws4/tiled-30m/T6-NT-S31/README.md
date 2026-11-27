# WS4 tiled 30-m dataset — T6|NT|S31

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `T6|NT|S31` (parent `T6|NT`)
- Tile / row / col: `T6` / 3 / 1
- Province: `NT`
- Centroid: 67.751782, -136.121453
- Allocated harvest: 73.941016 m3
- Productive subcell area: 64493.205159 ha
- Committed geometry area: 112438.852315 ha
- Clipped inventory geometry: 112438.852315 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 206920
- Blocks: 123309
- Forest area: 18622.80 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 7236
- Scheduled area: 1007.82 ha
- Eligible blocks (age class >= 40): 72352
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 4.00 MB
- Schedules: 0.08 MB
- Runs: 0.00 MB
- Total: 4.08 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
