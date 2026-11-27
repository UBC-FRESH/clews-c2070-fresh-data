# WS4 tiled 30-m dataset — C21|ON|S33

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `C21|ON|S33` (parent `C21|ON`)
- Tile / row / col: `C21` / 3 / 3
- Province: `ON`
- Centroid: 48.649808, -84.598001
- Allocated harvest: 64363.313747 m3
- Productive subcell area: 224804.520499 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2375896
- Blocks: 975913
- Forest area: 213830.64 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 86703
- Scheduled area: 16570.44 ha
- Eligible blocks (age class >= 40): 867026
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 30.77 MB
- Schedules: 1.03 MB
- Runs: 0.00 MB
- Total: 31.80 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
