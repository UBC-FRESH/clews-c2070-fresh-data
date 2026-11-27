# WS4 tiled 30-m dataset — E29|NB|S13

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `E29|NB|S13` (parent `E29|NB`)
- Tile / row / col: `E29` / 1 / 3
- Province: `NB`
- Centroid: 47.363714, -68.456140
- Allocated harvest: 89418.943026 m3
- Productive subcell area: 87223.746845 ha
- Committed geometry area: 93384.738245 ha
- Clipped inventory geometry: 93384.738245 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 880307
- Blocks: 298885
- Forest area: 79227.63 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 24833
- Scheduled area: 5772.06 ha
- Eligible blocks (age class >= 40): 248327
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 10.84 MB
- Schedules: 0.29 MB
- Runs: 0.00 MB
- Total: 11.13 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
