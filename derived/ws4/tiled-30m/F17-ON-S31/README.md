# WS4 tiled 30-m dataset — F17|ON|S31

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `F17|ON|S31` (parent `F17|ON`)
- Tile / row / col: `F17` / 3 / 1
- Province: `ON`
- Centroid: 53.264825, -93.991690
- Allocated harvest: 31638.841841 m3
- Productive subcell area: 177536.195523 ha
- Committed geometry area: 220984.114502 ha
- Clipped inventory geometry: 220984.114502 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1876715
- Blocks: 686517
- Forest area: 168904.35 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 64154
- Scheduled area: 14553.09 ha
- Eligible blocks (age class >= 40): 641535
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 23.05 MB
- Schedules: 0.76 MB
- Runs: 0.00 MB
- Total: 23.81 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
