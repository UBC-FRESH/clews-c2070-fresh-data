# WS4 tiled 30-m dataset — B24|ON|S33

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `B24|ON|S33` (parent `B24|ON`)
- Tile / row / col: `B24` / 3 / 3
- Province: `ON`
- Centroid: 46.493938, -79.223810
- Allocated harvest: 58254.288697 m3
- Productive subcell area: 219396.910180 ha
- Committed geometry area: 213403.454967 ha
- Clipped inventory geometry: 213403.454967 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2115667
- Blocks: 653623
- Forest area: 190410.03 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 61533
- Scheduled area: 16701.57 ha
- Eligible blocks (age class >= 40): 615327
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 24.61 MB
- Schedules: 0.73 MB
- Runs: 0.00 MB
- Total: 25.33 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
