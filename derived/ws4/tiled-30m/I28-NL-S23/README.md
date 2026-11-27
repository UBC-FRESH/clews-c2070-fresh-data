# WS4 tiled 30-m dataset — I28|NL|S23

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `I28|NL|S23` (parent `I28|NL`)
- Tile / row / col: `I28` / 2 / 3
- Province: `NL`
- Centroid: 53.191394, -66.549277
- Allocated harvest: 5464.744545 m3
- Productive subcell area: 122896.429058 ha
- Committed geometry area: 230899.679287 ha
- Clipped inventory geometry: 230899.679287 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1500224
- Blocks: 556788
- Forest area: 135020.16 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 52052
- Scheduled area: 12818.43 ha
- Eligible blocks (age class >= 40): 520511
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 18.94 MB
- Schedules: 0.61 MB
- Runs: 0.00 MB
- Total: 19.56 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
