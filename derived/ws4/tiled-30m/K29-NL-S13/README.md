# WS4 tiled 30-m dataset — K29|NL|S13

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `K29|NL|S13` (parent `K29|NL`)
- Tile / row / col: `K29` / 1 / 3
- Province: `NL`
- Centroid: 54.572534, -62.708463
- Allocated harvest: 5634.433291 m3
- Productive subcell area: 117739.178400 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1999915
- Blocks: 855230
- Forest area: 179992.35 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 78523
- Scheduled area: 15622.38 ha
- Eligible blocks (age class >= 40): 785228
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 25.80 MB
- Schedules: 0.93 MB
- Runs: 0.00 MB
- Total: 26.73 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
