# WS4 tiled 30-m dataset — M9|NT|S23

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `M9|NT|S23` (parent `M9|NT`)
- Tile / row / col: `M9` / 2 / 3
- Province: `NT`
- Centroid: 60.969195, -115.027572
- Allocated harvest: 138.439066 m3
- Productive subcell area: 109450.097673 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 695418
- Blocks: 228806
- Forest area: 62587.62 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 19993
- Scheduled area: 5683.86 ha
- Eligible blocks (age class >= 40): 199922
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 8.63 MB
- Schedules: 0.23 MB
- Runs: 0.00 MB
- Total: 8.86 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
