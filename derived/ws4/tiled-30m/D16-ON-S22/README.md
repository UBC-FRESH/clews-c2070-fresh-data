# WS4 tiled 30-m dataset — D16|ON|S22

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `D16|ON|S22` (parent `D16|ON`)
- Tile / row / col: `D16` / 2 / 2
- Province: `ON`
- Centroid: 49.922196, -95.152659
- Allocated harvest: 3.648012 m3
- Productive subcell area: 17.672041 ha
- Committed geometry area: 23.799775 ha
- Clipped inventory geometry: 23.799775 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 45
- Blocks: 40
- Forest area: 4.05 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 39
- Scheduled area: 3.96 ha
- Eligible blocks (age class >= 40): 39
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 0.07 MB
- Schedules: 0.00 MB
- Runs: 0.00 MB
- Total: 0.07 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
