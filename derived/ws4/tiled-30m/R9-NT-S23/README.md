# WS4 tiled 30-m dataset — R9|NT|S23

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `R9|NT|S23` (parent `R9|NT`)
- Tile / row / col: `R9` / 2 / 3
- Province: `NT`
- Centroid: 67.463469, -120.633695
- Allocated harvest: 2.434093 m3
- Productive subcell area: 6546.152004 ha
- Committed geometry area: 244140.851003 ha
- Clipped inventory geometry: 244140.851003 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 58651
- Blocks: 43433
- Forest area: 5278.59 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 949
- Scheduled area: 96.75 ha
- Eligible blocks (age class >= 40): 9485
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 1.32 MB
- Schedules: 0.01 MB
- Runs: 0.00 MB
- Total: 1.33 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
