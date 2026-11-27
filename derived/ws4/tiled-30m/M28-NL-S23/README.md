# WS4 tiled 30-m dataset — M28|NL|S23

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `M28|NL|S23` (parent `M28|NL`)
- Tile / row / col: `M28` / 2 / 3
- Province: `NL`
- Centroid: 57.922930, -62.201557
- Allocated harvest: 188.427114 m3
- Productive subcell area: 2197.964556 ha
- Committed geometry area: 53185.589732 ha
- Clipped inventory geometry: 53185.589732 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 25783
- Blocks: 11140
- Forest area: 2320.47 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 2678
- Scheduled area: 409.14 ha
- Eligible blocks (age class >= 40): 2678
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 0.47 MB
- Schedules: 0.03 MB
- Runs: 0.00 MB
- Total: 0.50 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
