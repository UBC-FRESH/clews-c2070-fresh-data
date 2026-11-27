# WS4 tiled 30-m dataset — F7|BC|S11

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `F7|BC|S11` (parent `F7|BC`)
- Tile / row / col: `F7` / 1 / 1
- Province: `BC`
- Centroid: 50.254773, -115.586506
- Allocated harvest: 113596.902731 m3
- Productive subcell area: 171393.056571 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2089410
- Blocks: 921061
- Forest area: 188046.90 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 80757
- Scheduled area: 13798.08 ha
- Eligible blocks (age class >= 40): 807563
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 27.50 MB
- Schedules: 0.96 MB
- Runs: 0.00 MB
- Total: 28.46 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
