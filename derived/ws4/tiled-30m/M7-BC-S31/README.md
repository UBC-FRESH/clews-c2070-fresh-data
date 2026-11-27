# WS4 tiled 30-m dataset — M7|BC|S31

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `M7|BC|S31` (parent `M7|BC`)
- Tile / row / col: `M7` / 3 / 1
- Province: `BC`
- Centroid: 59.912087, -122.327894
- Allocated harvest: 27132.194159 m3
- Productive subcell area: 66852.384407 ha
- Committed geometry area: 93660.337209 ha
- Clipped inventory geometry: 93660.337209 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 683310
- Blocks: 303317
- Forest area: 61497.90 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 29108
- Scheduled area: 5507.01 ha
- Eligible blocks (age class >= 40): 291073
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 9.61 MB
- Schedules: 0.34 MB
- Runs: 0.00 MB
- Total: 9.95 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
