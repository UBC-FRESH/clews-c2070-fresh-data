# WS4 tiled 30-m dataset — N4|BC|S32

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `N4|BC|S32` (parent `N4|BC`)
- Tile / row / col: `N4` / 3 / 2
- Province: `BC`
- Centroid: 59.531926, -130.115569
- Allocated harvest: 44279.454431 m3
- Productive subcell area: 151492.572394 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1064509
- Blocks: 628235
- Forest area: 95805.81 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 56921
- Scheduled area: 8202.51 ha
- Eligible blocks (age class >= 40): 569207
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 16.12 MB
- Schedules: 0.67 MB
- Runs: 0.00 MB
- Total: 16.79 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
