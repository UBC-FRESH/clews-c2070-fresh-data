# WS4 tiled 30-m dataset — B25|ON|S11

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `B25|ON|S11` (parent `B25|ON`)
- Tile / row / col: `B25` / 1 / 1
- Province: `ON`
- Centroid: 45.540304, -78.879821
- Allocated harvest: 95678.107504 m3
- Productive subcell area: 331720.889573 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2451097
- Blocks: 634134
- Forest area: 220598.73 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 61692
- Scheduled area: 18558.81 ha
- Eligible blocks (age class >= 40): 616920
- Simulated years: 20
- Harvested volume: 3456426.024 m3
- Treated/managed area: 18558.810 ha

## Storage

- Dataset: 26.74 MB
- Schedules: 0.73 MB
- Runs: 20.01 MB
- Total: 47.47 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
