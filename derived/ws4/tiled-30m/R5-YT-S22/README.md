# WS4 tiled 30-m dataset — R5|YT|S22

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `R5|YT|S22` (parent `R5|YT`)
- Tile / row / col: `R5` / 2 / 2
- Province: `YT`
- Centroid: 64.548806, -133.573603
- Allocated harvest: 90.957357 m3
- Productive subcell area: 80876.187528 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 633340
- Blocks: 277798
- Forest area: 57000.60 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 20329
- Scheduled area: 4350.87 ha
- Eligible blocks (age class >= 40): 203283
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 8.85 MB
- Schedules: 0.24 MB
- Runs: 0.00 MB
- Total: 9.08 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
