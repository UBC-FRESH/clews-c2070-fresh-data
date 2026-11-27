# WS4 tiled 30-m dataset — L28|NL|S33

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `L28|NL|S33` (parent `L28|NL`)
- Tile / row / col: `L28` / 3 / 3
- Province: `NL`
- Centroid: 57.245595, -62.870393
- Allocated harvest: 1359.386126 m3
- Productive subcell area: 26934.572360 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 356514
- Blocks: 140815
- Forest area: 32086.26 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 9512
- Scheduled area: 2324.97 ha
- Eligible blocks (age class >= 40): 95111
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 5.28 MB
- Schedules: 0.11 MB
- Runs: 0.00 MB
- Total: 5.38 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
