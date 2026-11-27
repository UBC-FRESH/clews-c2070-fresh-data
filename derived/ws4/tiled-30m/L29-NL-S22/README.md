# WS4 tiled 30-m dataset — L29|NL|S22

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `L29|NL|S22` (parent `L29|NL`)
- Tile / row / col: `L29` / 2 / 2
- Province: `NL`
- Centroid: 56.383418, -61.866243
- Allocated harvest: 4756.561286 m3
- Productive subcell area: 62693.422860 ha
- Committed geometry area: 164914.475537 ha
- Clipped inventory geometry: 164914.475537 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 939181
- Blocks: 332592
- Forest area: 84526.29 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 25186
- Scheduled area: 6337.80 ha
- Eligible blocks (age class >= 40): 251851
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 11.32 MB
- Schedules: 0.29 MB
- Runs: 0.00 MB
- Total: 11.62 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
