# WS4 tiled 30-m dataset — G11|SK|S23

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `G11|SK|S23` (parent `G11|SK`)
- Tile / row / col: `G11` / 2 / 3
- Province: `SK`
- Centroid: 53.601643, -106.349177
- Allocated harvest: 32819.653730 m3
- Productive subcell area: 139868.653356 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1594442
- Blocks: 630037
- Forest area: 143499.78 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 56219
- Scheduled area: 11982.78 ha
- Eligible blocks (age class >= 40): 562189
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 20.43 MB
- Schedules: 0.66 MB
- Runs: 0.00 MB
- Total: 21.09 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
