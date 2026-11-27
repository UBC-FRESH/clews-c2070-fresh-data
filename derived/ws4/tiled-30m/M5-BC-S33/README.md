# WS4 tiled 30-m dataset — M5|BC|S33

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `M5|BC|S33` (parent `M5|BC`)
- Tile / row / col: `M5` / 3 / 3
- Province: `BC`
- Centroid: 59.240256, -125.628765
- Allocated harvest: 44439.105201 m3
- Productive subcell area: 135935.973745 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2201703
- Blocks: 993388
- Forest area: 198153.27 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 94882
- Scheduled area: 18162.36 ha
- Eligible blocks (age class >= 40): 948816
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 29.38 MB
- Schedules: 1.13 MB
- Runs: 0.00 MB
- Total: 30.51 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
