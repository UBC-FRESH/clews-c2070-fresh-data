# WS4 tiled 30-m dataset — M28|NL|S32

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `M28|NL|S32` (parent `M28|NL`)
- Tile / row / col: `M28` / 3 / 2
- Province: `NL`
- Centroid: 58.487981, -62.592520
- Allocated harvest: 16.406282 m3
- Productive subcell area: 191.375993 ha
- Committed geometry area: 4630.850403 ha
- Clipped inventory geometry: 4630.850403 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 467
- Blocks: 345
- Forest area: 42.03 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 24
- Scheduled area: 2.43 ha
- Eligible blocks (age class >= 40): 24
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
