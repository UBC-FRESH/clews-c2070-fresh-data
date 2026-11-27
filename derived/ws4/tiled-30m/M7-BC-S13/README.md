# WS4 tiled 30-m dataset — M7|BC|S13

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `M7|BC|S13` (parent `M7|BC`)
- Tile / row / col: `M7` / 1 / 3
- Province: `BC`
- Centroid: 59.562339, -120.194423
- Allocated harvest: 31108.636759 m3
- Productive subcell area: 76650.142292 ha
- Committed geometry area: 107387.017499 ha
- Clipped inventory geometry: 107387.017499 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 467809
- Blocks: 181465
- Forest area: 42102.81 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 14072
- Scheduled area: 2503.89 ha
- Eligible blocks (age class >= 40): 140719
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 6.42 MB
- Schedules: 0.16 MB
- Runs: 0.00 MB
- Total: 6.58 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
