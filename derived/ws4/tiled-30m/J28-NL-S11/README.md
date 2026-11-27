# WS4 tiled 30-m dataset — J28|NL|S11

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `J28|NL|S11` (parent `J28|NL`)
- Tile / row / col: `J28` / 1 / 1
- Province: `NL`
- Centroid: 54.364247, -67.247393
- Allocated harvest: 4415.942628 m3
- Productive subcell area: 107879.521888 ha
- Committed geometry area: 214334.596801 ha
- Clipped inventory geometry: 214334.596801 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1115592
- Blocks: 571991
- Forest area: 100403.28 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 43538
- Scheduled area: 8064.18 ha
- Eligible blocks (age class >= 40): 435373
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 15.99 MB
- Schedules: 0.51 MB
- Runs: 0.00 MB
- Total: 16.50 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
