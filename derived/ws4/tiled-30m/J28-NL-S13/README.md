# WS4 tiled 30-m dataset — J28|NL|S13

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `J28|NL|S13` (parent `J28|NL`)
- Tile / row / col: `J28` / 1 / 3
- Province: `NL`
- Centroid: 53.994561, -65.872063
- Allocated harvest: 5150.758083 m3
- Productive subcell area: 125830.737896 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1599206
- Blocks: 424767
- Forest area: 143928.54 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 38192
- Scheduled area: 16936.47 ha
- Eligible blocks (age class >= 40): 381915
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 16.87 MB
- Schedules: 0.45 MB
- Runs: 0.00 MB
- Total: 17.32 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
