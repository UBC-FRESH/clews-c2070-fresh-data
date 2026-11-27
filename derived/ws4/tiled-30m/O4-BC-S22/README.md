# WS4 tiled 30-m dataset — O4|BC|S22

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `O4|BC|S22` (parent `O4|BC`)
- Tile / row / col: `O4` / 2 / 2
- Province: `BC`
- Centroid: 59.998658, -131.230220
- Allocated harvest: 2.885188 m3
- Productive subcell area: 15.957294 ha
- Committed geometry area: 29.246380 ha
- Clipped inventory geometry: 29.246380 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 311
- Blocks: 187
- Forest area: 27.99 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 187
- Scheduled area: 27.99 ha
- Eligible blocks (age class >= 40): 187
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 0.08 MB
- Schedules: 0.00 MB
- Runs: 0.00 MB
- Total: 0.08 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
