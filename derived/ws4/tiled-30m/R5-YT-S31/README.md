# WS4 tiled 30-m dataset — R5|YT|S31

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `R5|YT|S31` (parent `R5|YT`)
- Tile / row / col: `R5` / 3 / 1
- Province: `YT`
- Centroid: 64.657655, -135.075934
- Allocated harvest: 90.957357 m3
- Productive subcell area: 80876.187528 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 486375
- Blocks: 218733
- Forest area: 43773.75 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 14705
- Scheduled area: 3215.25 ha
- Eligible blocks (age class >= 40): 147047
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 7.11 MB
- Schedules: 0.17 MB
- Runs: 0.00 MB
- Total: 7.28 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
