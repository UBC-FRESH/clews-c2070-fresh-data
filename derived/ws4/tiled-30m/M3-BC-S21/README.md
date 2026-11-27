# WS4 tiled 30-m dataset — M3|BC|S21

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `M3|BC|S21` (parent `M3|BC`)
- Tile / row / col: `M3` / 2 / 1
- Province: `BC`
- Centroid: 56.991520, -131.217108
- Allocated harvest: 43400.428067 m3
- Productive subcell area: 115077.884728 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 544924
- Blocks: 286348
- Forest area: 49043.16 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 25762
- Scheduled area: 4283.28 ha
- Eligible blocks (age class >= 40): 257618
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 8.38 MB
- Schedules: 0.30 MB
- Runs: 0.00 MB
- Total: 8.68 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
