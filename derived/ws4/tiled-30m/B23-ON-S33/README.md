# WS4 tiled 30-m dataset — B23|ON|S33

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `B23|ON|S33` (parent `B23|ON`)
- Tile / row / col: `B23` / 3 / 3
- Province: `ON`
- Centroid: 46.821015, -81.069125
- Allocated harvest: 63826.754836 m3
- Productive subcell area: 211174.078444 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2339994
- Blocks: 886420
- Forest area: 210599.46 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 78490
- Scheduled area: 17190.99 ha
- Eligible blocks (age class >= 40): 784897
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 29.56 MB
- Schedules: 0.93 MB
- Runs: 0.00 MB
- Total: 30.50 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
