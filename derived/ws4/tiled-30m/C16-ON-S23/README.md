# WS4 tiled 30-m dataset — C16|ON|S23

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `C16|ON|S23` (parent `C16|ON`)
- Tile / row / col: `C16` / 2 / 3
- Province: `ON`
- Centroid: 48.830189, -94.560942
- Allocated harvest: 6083.760116 m3
- Productive subcell area: 29005.660067 ha
- Committed geometry area: 36871.107910 ha
- Clipped inventory geometry: 36871.107910 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 285993
- Blocks: 88462
- Forest area: 25739.37 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 6695
- Scheduled area: 2097.90 ha
- Eligible blocks (age class >= 40): 66950
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 3.89 MB
- Schedules: 0.07 MB
- Runs: 0.00 MB
- Total: 3.96 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
