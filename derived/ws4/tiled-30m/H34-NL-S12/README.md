# WS4 tiled 30-m dataset — H34|NL|S12

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `H34|NL|S12` (parent `H34|NL`)
- Tile / row / col: `H34` / 1 / 2
- Province: `NL`
- Centroid: 47.813551, -57.486442
- Allocated harvest: 6614.546074 m3
- Productive subcell area: 109134.477312 ha
- Committed geometry area: 216629.950134 ha
- Clipped inventory geometry: 216629.950134 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 927812
- Blocks: 534902
- Forest area: 83503.08 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 38263
- Scheduled area: 6027.39 ha
- Eligible blocks (age class >= 40): 382621
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 14.13 MB
- Schedules: 0.45 MB
- Runs: 0.00 MB
- Total: 14.58 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
