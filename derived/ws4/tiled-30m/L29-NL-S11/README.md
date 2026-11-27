# WS4 tiled 30-m dataset — L29|NL|S11

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `L29|NL|S11` (parent `L29|NL`)
- Tile / row / col: `L29` / 1 / 1
- Province: `NL`
- Centroid: 56.219040, -62.946794
- Allocated harvest: 7210.648536 m3
- Productive subcell area: 95039.296363 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 629208
- Blocks: 262094
- Forest area: 56628.72 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 16836
- Scheduled area: 3562.74 ha
- Eligible blocks (age class >= 40): 168352
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 8.65 MB
- Schedules: 0.20 MB
- Runs: 0.00 MB
- Total: 8.85 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
