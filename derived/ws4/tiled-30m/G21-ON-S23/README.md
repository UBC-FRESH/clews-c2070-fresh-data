# WS4 tiled 30-m dataset — G21|ON|S23

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `G21|ON|S23` (parent `G21|ON`)
- Tile / row / col: `G21` / 2 / 3
- Province: `ON`
- Centroid: 53.555167, -83.225933
- Allocated harvest: 7752.746737 m3
- Productive subcell area: 117612.074200 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1123849
- Blocks: 627681
- Forest area: 101146.41 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 54248
- Scheduled area: 8950.05 ha
- Eligible blocks (age class >= 40): 542480
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 16.68 MB
- Schedules: 0.64 MB
- Runs: 0.00 MB
- Total: 17.32 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
