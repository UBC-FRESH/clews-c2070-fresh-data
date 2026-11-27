# WS4 tiled 30-m dataset — M29|NL|S11

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `M29|NL|S11` (parent `M29|NL`)
- Tile / row / col: `M29` / 1 / 1
- Province: `NL`
- Centroid: 57.400061, -61.885433
- Allocated harvest: 3098.493532 m3
- Productive subcell area: 35844.105899 ha
- Committed geometry area: 94635.022711 ha
- Clipped inventory geometry: 94635.022711 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 318532
- Blocks: 131073
- Forest area: 28667.88 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 9162
- Scheduled area: 2191.95 ha
- Eligible blocks (age class >= 40): 91612
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 4.93 MB
- Schedules: 0.10 MB
- Runs: 0.00 MB
- Total: 5.04 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
