# WS4 tiled 30-m dataset — D20|ON|S22

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `D20|ON|S22` (parent `D20|ON`)
- Tile / row / col: `D20` / 2 / 2
- Province: `ON`
- Centroid: 49.798447, -87.121038
- Allocated harvest: 48678.315136 m3
- Productive subcell area: 212302.677765 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2308026
- Blocks: 908364
- Forest area: 207722.34 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 81970
- Scheduled area: 16554.96 ha
- Eligible blocks (age class >= 40): 819692
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 29.37 MB
- Schedules: 0.97 MB
- Runs: 0.00 MB
- Total: 30.34 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
