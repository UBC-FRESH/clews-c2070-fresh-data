# WS4 tiled 30-m dataset — M7|BC|S22

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `M7|BC|S22` (parent `M7|BC`)
- Tile / row / col: `M7` / 2 / 2
- Province: `BC`
- Centroid: 59.796092, -121.147491
- Allocated harvest: 65330.890243 m3
- Productive subcell area: 160972.082192 ha
- Committed geometry area: 225522.240277 ha
- Clipped inventory geometry: 225522.240277 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1642389
- Blocks: 291066
- Forest area: 147815.01 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 17935
- Scheduled area: 3571.83 ha
- Eligible blocks (age class >= 40): 179341
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 14.63 MB
- Schedules: 0.21 MB
- Runs: 0.00 MB
- Total: 14.84 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
