# WS4 tiled 30-m dataset — B27|ON|S32

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `B27|ON|S32` (parent `B27|ON`)
- Tile / row / col: `B27` / 3 / 2
- Province: `ON`
- Centroid: 45.459511, -74.527269
- Allocated harvest: 2836.762180 m3
- Productive subcell area: 8546.883499 ha
- Committed geometry area: 50122.428059 ha
- Clipped inventory geometry: 50122.428059 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 185567
- Blocks: 65866
- Forest area: 16701.03 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 4266
- Scheduled area: 1116.72 ha
- Eligible blocks (age class >= 40): 42657
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 2.75 MB
- Schedules: 0.05 MB
- Runs: 0.00 MB
- Total: 2.80 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
