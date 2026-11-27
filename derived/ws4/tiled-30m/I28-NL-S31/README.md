# WS4 tiled 30-m dataset — I28|NL|S31

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `I28|NL|S31` (parent `I28|NL`)
- Tile / row / col: `I28` / 3 / 1
- Province: `NL`
- Centroid: 53.995084, -67.461153
- Allocated harvest: 3415.711754 m3
- Productive subcell area: 76815.809746 ha
- Committed geometry area: 144322.711169 ha
- Clipped inventory geometry: 144322.711169 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 827030
- Blocks: 360930
- Forest area: 74432.70 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 31139
- Scheduled area: 6567.39 ha
- Eligible blocks (age class >= 40): 311382
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 11.26 MB
- Schedules: 0.37 MB
- Runs: 0.00 MB
- Total: 11.63 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
