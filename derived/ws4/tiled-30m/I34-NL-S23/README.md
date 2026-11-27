# WS4 tiled 30-m dataset — I34|NL|S23

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `I34|NL|S23` (parent `I34|NL`)
- Tile / row / col: `I34` / 2 / 3
- Province: `NL`
- Centroid: 48.998261, -55.398220
- Allocated harvest: 13381.379719 m3
- Productive subcell area: 173749.551289 ha
- Committed geometry area: 243028.023107 ha
- Clipped inventory geometry: 243028.023107 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2080301
- Blocks: 892336
- Forest area: 187227.09 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 79168
- Scheduled area: 15108.21 ha
- Eligible blocks (age class >= 40): 791671
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 27.00 MB
- Schedules: 0.94 MB
- Runs: 0.00 MB
- Total: 27.94 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
