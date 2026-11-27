# WS4 tiled 30-m dataset — I34|NL|S11

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `I34|NL|S11` (parent `I34|NL`)
- Tile / row / col: `I34` / 1 / 1
- Province: `NL`
- Centroid: 49.149990, -56.910068
- Allocated harvest: 13765.264133 m3
- Productive subcell area: 178734.070528 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1432505
- Blocks: 675327
- Forest area: 128925.45 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 58711
- Scheduled area: 9434.88 ha
- Eligible blocks (age class >= 40): 587107
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 19.77 MB
- Schedules: 0.69 MB
- Runs: 0.00 MB
- Total: 20.47 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
