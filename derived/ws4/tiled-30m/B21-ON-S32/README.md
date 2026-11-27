# WS4 tiled 30-m dataset — B21|ON|S32

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `B21|ON|S32` (parent `B21|ON`)
- Tile / row / col: `B21` / 3 / 2
- Province: `ON`
- Centroid: 47.360385, -85.808836
- Allocated harvest: 239.706046 m3
- Productive subcell area: 634.027065 ha
- Committed geometry area: 691.536660 ha
- Clipped inventory geometry: 691.536660 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 6284
- Blocks: 2768
- Forest area: 565.56 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 2560
- Scheduled area: 536.67 ha
- Eligible blocks (age class >= 40): 2560
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 0.17 MB
- Schedules: 0.02 MB
- Runs: 0.00 MB
- Total: 0.19 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
