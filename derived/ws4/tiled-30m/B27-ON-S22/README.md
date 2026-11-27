# WS4 tiled 30-m dataset — B27|ON|S22

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `B27|ON|S22` (parent `B27|ON`)
- Tile / row / col: `B27` / 2 / 2
- Province: `ON`
- Centroid: 45.179848, -74.615931
- Allocated harvest: 5072.077991 m3
- Productive subcell area: 15281.668657 ha
- Committed geometry area: 89617.968693 ha
- Clipped inventory geometry: 89617.968693 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 487416
- Blocks: 155608
- Forest area: 43867.44 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 10971
- Scheduled area: 3004.56 ha
- Eligible blocks (age class >= 40): 109701
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 6.31 MB
- Schedules: 0.12 MB
- Runs: 0.00 MB
- Total: 6.44 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
