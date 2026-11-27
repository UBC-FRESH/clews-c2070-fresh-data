# WS4 tiled 30-m dataset — M5|BC|S22

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `M5|BC|S22` (parent `M5|BC`)
- Tile / row / col: `M5` / 2 / 2
- Province: `BC`
- Centroid: 58.617446, -126.002606
- Allocated harvest: 44439.105201 m3
- Productive subcell area: 135935.973745 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1125045
- Blocks: 635676
- Forest area: 101254.05 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 57338
- Scheduled area: 8877.15 ha
- Eligible blocks (age class >= 40): 573377
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 17.02 MB
- Schedules: 0.68 MB
- Runs: 0.00 MB
- Total: 17.70 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
