# WS4 tiled 30-m dataset — R9|NT|S12

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `R9|NT|S12` (parent `R9|NT`)
- Tile / row / col: `R9` / 1 / 2
- Province: `NT`
- Centroid: 66.862414, -121.246467
- Allocated harvest: 2.492509 m3
- Productive subcell area: 6703.253447 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 443783
- Blocks: 205421
- Forest area: 39940.47 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 13370
- Scheduled area: 2237.49 ha
- Eligible blocks (age class >= 40): 133696
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 6.56 MB
- Schedules: 0.15 MB
- Runs: 0.00 MB
- Total: 6.71 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
