# WS4 tiled 30-m dataset — K14|SK|S11

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `K14|SK|S11` (parent `K14|SK`)
- Tile / row / col: `K14` / 1 / 1
- Province: `SK`
- Centroid: 59.056895, -102.189479
- Allocated harvest: 4625.792145 m3
- Productive subcell area: 59147.074970 ha
- Committed geometry area: 102082.319407 ha
- Clipped inventory geometry: 102082.319407 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 603184
- Blocks: 141721
- Forest area: 54286.56 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 9000
- Scheduled area: 4628.61 ha
- Eligible blocks (age class >= 40): 89995
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 6.49 MB
- Schedules: 0.10 MB
- Runs: 0.00 MB
- Total: 6.59 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
