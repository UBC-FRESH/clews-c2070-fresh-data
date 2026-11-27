# WS4 tiled 30-m dataset — D16|ON|S13

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `D16|ON|S13` (parent `D16|ON`)
- Tile / row / col: `D16` / 1 / 3
- Province: `ON`
- Centroid: 49.700198, -94.828431
- Allocated harvest: 25879.342573 m3
- Productive subcell area: 125367.119599 ha
- Committed geometry area: 168837.840775 ha
- Clipped inventory geometry: 168837.840775 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1476831
- Blocks: 692651
- Forest area: 132914.79 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 64768
- Scheduled area: 12082.32 ha
- Eligible blocks (age class >= 40): 647674
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 20.44 MB
- Schedules: 0.77 MB
- Runs: 0.00 MB
- Total: 21.20 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
