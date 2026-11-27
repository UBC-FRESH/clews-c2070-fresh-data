# WS4 tiled 30-m dataset — I34|NL|S12

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `I34|NL|S12` (parent `I34|NL`)
- Tile / row / col: `I34` / 1 / 2
- Province: `NL`
- Centroid: 48.894892, -56.347057
- Allocated harvest: 13765.264133 m3
- Productive subcell area: 178734.070528 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1825976
- Blocks: 774118
- Forest area: 164337.84 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 67139
- Scheduled area: 12910.14 ha
- Eligible blocks (age class >= 40): 671389
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 23.77 MB
- Schedules: 0.80 MB
- Runs: 0.00 MB
- Total: 24.56 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
