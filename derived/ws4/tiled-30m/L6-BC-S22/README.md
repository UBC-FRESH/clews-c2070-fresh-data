# WS4 tiled 30-m dataset — L6|BC|S22

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `L6|BC|S22` (parent `L6|BC`)
- Tile / row / col: `L6` / 2 / 2
- Province: `BC`
- Centroid: 57.991897, -122.484014
- Allocated harvest: 105462.722577 m3
- Productive subcell area: 228674.244542 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2715384
- Blocks: 1238966
- Forest area: 244384.56 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 121520
- Scheduled area: 22796.10 ha
- Eligible blocks (age class >= 40): 1215192
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 37.02 MB
- Schedules: 1.47 MB
- Runs: 0.00 MB
- Total: 38.49 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
