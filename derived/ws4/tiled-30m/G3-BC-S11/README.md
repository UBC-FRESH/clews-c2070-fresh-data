# WS4 tiled 30-m dataset — G3|BC|S11

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `G3|BC|S11` (parent `G3|BC`)
- Tile / row / col: `G3` / 1 / 1
- Province: `BC`
- Centroid: 49.272982, -124.287106
- Allocated harvest: 53506.353166 m3
- Productive subcell area: 61327.543338 ha
- Committed geometry area: 86307.484587 ha
- Clipped inventory geometry: 86307.484587 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 808886
- Blocks: 330624
- Forest area: 72799.74 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 30385
- Scheduled area: 5929.02 ha
- Eligible blocks (age class >= 40): 303849
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 10.75 MB
- Schedules: 0.35 MB
- Runs: 0.00 MB
- Total: 11.10 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
