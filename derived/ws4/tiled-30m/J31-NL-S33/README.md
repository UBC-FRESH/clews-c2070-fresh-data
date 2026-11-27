# WS4 tiled 30-m dataset — J31|NL|S33

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `J31|NL|S33` (parent `J31|NL`)
- Tile / row / col: `J31` / 3 / 3
- Province: `NL`
- Centroid: 52.781822, -59.135303
- Allocated harvest: 14899.999541 m3
- Productive subcell area: 207854.013281 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2129928
- Blocks: 629664
- Forest area: 191693.52 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 58342
- Scheduled area: 18689.31 ha
- Eligible blocks (age class >= 40): 583416
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 23.99 MB
- Schedules: 0.69 MB
- Runs: 0.00 MB
- Total: 24.68 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
