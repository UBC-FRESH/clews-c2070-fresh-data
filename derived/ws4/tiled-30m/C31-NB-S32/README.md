# WS4 tiled 30-m dataset — C31|NB|S32

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `C31|NB|S32` (parent `C31|NB`)
- Tile / row / col: `C31` / 3 / 2
- Province: `NB`
- Centroid: 44.701155, -66.805584
- Allocated harvest: 12163.664797 m3
- Productive subcell area: 15018.344039 ha
- Committed geometry area: 16808.761411 ha
- Clipped inventory geometry: 16808.761411 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 161799
- Blocks: 79357
- Forest area: 14561.91 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 7344
- Scheduled area: 1314.45 ha
- Eligible blocks (age class >= 40): 73437
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 2.89 MB
- Schedules: 0.08 MB
- Runs: 0.00 MB
- Total: 2.97 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
