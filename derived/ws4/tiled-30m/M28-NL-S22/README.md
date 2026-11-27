# WS4 tiled 30-m dataset — M28|NL|S22

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `M28|NL|S22` (parent `M28|NL`)
- Tile / row / col: `M28` / 2 / 2
- Province: `NL`
- Centroid: 58.247011, -62.886929
- Allocated harvest: 557.708533 m3
- Productive subcell area: 6505.558365 ha
- Committed geometry area: 157419.261932 ha
- Clipped inventory geometry: 157419.261932 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 36289
- Blocks: 21404
- Forest area: 3266.01 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 768
- Scheduled area: 109.62 ha
- Eligible blocks (age class >= 40): 7675
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 0.75 MB
- Schedules: 0.01 MB
- Runs: 0.00 MB
- Total: 0.76 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
