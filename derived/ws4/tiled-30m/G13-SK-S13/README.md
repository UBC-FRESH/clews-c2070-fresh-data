# WS4 tiled 30-m dataset — G13|SK|S13

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `G13|SK|S13` (parent `G13|SK`)
- Tile / row / col: `G13` / 1 / 3
- Province: `SK`
- Centroid: 53.527200, -101.902095
- Allocated harvest: 17526.187492 m3
- Productive subcell area: 78020.601354 ha
- Committed geometry area: 109526.431498 ha
- Clipped inventory geometry: 109526.431498 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 893357
- Blocks: 382453
- Forest area: 80402.13 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 36346
- Scheduled area: 7639.38 ha
- Eligible blocks (age class >= 40): 363455
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 12.04 MB
- Schedules: 0.43 MB
- Runs: 0.00 MB
- Total: 12.46 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
