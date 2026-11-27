# WS4 tiled 30-m dataset — B21|ON|S33

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `B21|ON|S33` (parent `B21|ON`)
- Tile / row / col: `B21` / 3 / 3
- Province: `ON`
- Centroid: 47.382825, -84.691861
- Allocated harvest: 16422.488042 m3
- Productive subcell area: 43437.794254 ha
- Committed geometry area: 47377.831005 ha
- Clipped inventory geometry: 47377.831005 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 502070
- Blocks: 100967
- Forest area: 45186.30 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 9946
- Scheduled area: 3205.62 ha
- Eligible blocks (age class >= 40): 99453
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 5.42 MB
- Schedules: 0.11 MB
- Runs: 0.00 MB
- Total: 5.53 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
