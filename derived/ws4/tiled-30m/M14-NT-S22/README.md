# WS4 tiled 30-m dataset — M14|NT|S22

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `M14|NT|S22` (parent `M14|NT`)
- Tile / row / col: `M14` / 2 / 2
- Province: `NT`
- Centroid: 62.328449, -102.096227
- Allocated harvest: 1.971934 m3
- Productive subcell area: 5150.024518 ha
- Committed geometry area: 47331.519713 ha
- Clipped inventory geometry: 47331.519713 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 8965
- Blocks: 7223
- Forest area: 806.85 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 3015
- Scheduled area: 328.23 ha
- Eligible blocks (age class >= 40): 3015
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 0.26 MB
- Schedules: 0.03 MB
- Runs: 0.00 MB
- Total: 0.29 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
