# WS4 tiled 30-m dataset — D17|ON|S22

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `D17|ON|S22` (parent `D17|ON`)
- Tile / row / col: `D17` / 2 / 2
- Province: `ON`
- Centroid: 50.101121, -93.398584
- Allocated harvest: 44486.455537 m3
- Productive subcell area: 192442.146404 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2158498
- Blocks: 846562
- Forest area: 194264.82 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 76656
- Scheduled area: 15581.79 ha
- Eligible blocks (age class >= 40): 766553
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 27.00 MB
- Schedules: 0.91 MB
- Runs: 0.00 MB
- Total: 27.91 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
