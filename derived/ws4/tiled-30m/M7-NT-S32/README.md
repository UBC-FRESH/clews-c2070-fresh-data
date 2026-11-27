# WS4 tiled 30-m dataset — M7|NT|S32

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `M7|NT|S32` (parent `M7|NT`)
- Tile / row / col: `M7` / 3 / 2
- Province: `NT`
- Centroid: 60.249428, -121.505331
- Allocated harvest: 261.626568 m3
- Productive subcell area: 166265.449524 ha
- Committed geometry area: 243918.732264 ha
- Clipped inventory geometry: 243918.732264 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1689340
- Blocks: 518885
- Forest area: 152040.60 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 41487
- Scheduled area: 7691.49 ha
- Eligible blocks (age class >= 40): 414865
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 18.83 MB
- Schedules: 0.49 MB
- Runs: 0.00 MB
- Total: 19.32 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
