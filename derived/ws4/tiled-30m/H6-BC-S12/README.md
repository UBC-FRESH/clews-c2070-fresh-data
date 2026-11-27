# WS4 tiled 30-m dataset — H6|BC|S12

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `H6|BC|S12` (parent `H6|BC`)
- Tile / row / col: `H6` / 1 / 2
- Province: `BC`
- Centroid: 52.482184, -118.496314
- Allocated harvest: 66713.746634 m3
- Productive subcell area: 113114.220105 ha
- Committed geometry area: 190166.214992 ha
- Clipped inventory geometry: 190166.214992 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1060938
- Blocks: 558797
- Forest area: 95484.42 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 51936
- Scheduled area: 7746.39 ha
- Eligible blocks (age class >= 40): 519357
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 15.23 MB
- Schedules: 0.61 MB
- Runs: 0.00 MB
- Total: 15.84 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
