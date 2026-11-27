# WS4 tiled 30-m dataset — I4|BC|S32

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `I4|BC|S32` (parent `I4|BC`)
- Tile / row / col: `I4` / 3 / 2
- Province: `BC`
- Centroid: 53.497126, -124.089196
- Allocated harvest: 121739.863305 m3
- Productive subcell area: 226249.614180 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2600001
- Blocks: 648767
- Forest area: 234000.09 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 55399
- Scheduled area: 10616.22 ha
- Eligible blocks (age class >= 40): 553985
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 26.27 MB
- Schedules: 0.66 MB
- Runs: 0.00 MB
- Total: 26.93 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
