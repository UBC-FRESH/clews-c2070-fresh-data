# WS4 tiled 30-m dataset — J31|NL|S21

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `J31|NL|S21` (parent `J31|NL`)
- Tile / row / col: `J31` / 2 / 1
- Province: `NL`
- Centroid: 52.870330, -60.809592
- Allocated harvest: 14899.999541 m3
- Productive subcell area: 207854.013281 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2340512
- Blocks: 661252
- Forest area: 210646.08 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 64264
- Scheduled area: 19580.94 ha
- Eligible blocks (age class >= 40): 642638
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 26.42 MB
- Schedules: 0.76 MB
- Runs: 0.00 MB
- Total: 27.18 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
