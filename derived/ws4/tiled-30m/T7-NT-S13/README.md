# WS4 tiled 30-m dataset — T7|NT|S13

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `T7|NT|S13` (parent `T7|NT`)
- Tile / row / col: `T7` / 1 / 3
- Province: `NT`
- Centroid: 68.252747, -129.962552
- Allocated harvest: 143.457501 m3
- Productive subcell area: 147355.144971 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1926808
- Blocks: 651253
- Forest area: 173412.72 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 50284
- Scheduled area: 10291.05 ha
- Eligible blocks (age class >= 40): 502836
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 22.32 MB
- Schedules: 0.59 MB
- Runs: 0.00 MB
- Total: 22.91 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
