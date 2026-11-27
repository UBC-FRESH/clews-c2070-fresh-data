# WS4 tiled 30-m dataset — M14|NT|S21

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `M14|NT|S21` (parent `M14|NT`)
- Tile / row / col: `M14` / 2 / 1
- Province: `NT`
- Centroid: 62.274086, -102.680133
- Allocated harvest: 10.415544 m3
- Productive subcell area: 27201.875986 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 79355
- Blocks: 57317
- Forest area: 7141.95 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 2560
- Scheduled area: 329.76 ha
- Eligible blocks (age class >= 40): 25598
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 1.78 MB
- Schedules: 0.03 MB
- Runs: 0.00 MB
- Total: 1.81 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
