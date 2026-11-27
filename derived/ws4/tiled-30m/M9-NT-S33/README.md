# WS4 tiled 30-m dataset — M9|NT|S33

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `M9|NT|S33` (parent `M9|NT`)
- Tile / row / col: `M9` / 3 / 3
- Province: `NT`
- Centroid: 61.408335, -115.326261
- Allocated harvest: 138.439066 m3
- Productive subcell area: 109450.097673 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 67731
- Blocks: 30053
- Forest area: 6095.79 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 1466
- Scheduled area: 373.41 ha
- Eligible blocks (age class >= 40): 14653
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 1.18 MB
- Schedules: 0.02 MB
- Runs: 0.00 MB
- Total: 1.20 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
