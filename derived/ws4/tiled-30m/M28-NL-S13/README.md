# WS4 tiled 30-m dataset — M28|NL|S13

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `M28|NL|S13` (parent `M28|NL`)
- Tile / row / col: `M28` / 1 / 3
- Province: `NL`
- Centroid: 57.653514, -62.476305
- Allocated harvest: 817.863701 m3
- Productive subcell area: 9540.216313 ha
- Committed geometry area: 230850.870367 ha
- Clipped inventory geometry: 230850.870367 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 570100
- Blocks: 200812
- Forest area: 51309.00 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 13650
- Scheduled area: 3818.97 ha
- Eligible blocks (age class >= 40): 136496
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 7.44 MB
- Schedules: 0.16 MB
- Runs: 0.00 MB
- Total: 7.60 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
