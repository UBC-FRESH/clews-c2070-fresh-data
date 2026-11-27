# WS4 tiled 30-m dataset — N14|NT|S32

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `N14|NT|S32` (parent `N14|NT`)
- Tile / row / col: `N14` / 3 / 2
- Province: `NT`
- Centroid: 64.078876, -102.343563
- Allocated harvest: 0.190372 m3
- Productive subcell area: 397.759060 ha
- Committed geometry area: 99566.099293 ha
- Clipped inventory geometry: 99566.099293 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 26630
- Blocks: 16669
- Forest area: 2396.70 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 725
- Scheduled area: 99.90 ha
- Eligible blocks (age class >= 40): 7244
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 0.58 MB
- Schedules: 0.01 MB
- Runs: 0.00 MB
- Total: 0.59 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
