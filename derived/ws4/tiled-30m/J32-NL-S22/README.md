# WS4 tiled 30-m dataset — J32|NL|S22

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `J32|NL|S22` (parent `J32|NL`)
- Tile / row / col: `J32` / 2 / 2
- Province: `NL`
- Centroid: 52.072346, -58.286446
- Allocated harvest: 3064.848982 m3
- Productive subcell area: 52339.931107 ha
- Committed geometry area: 67075.082133 ha
- Clipped inventory geometry: 67075.082133 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 641660
- Blocks: 231412
- Forest area: 57749.40 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 22158
- Scheduled area: 5122.89 ha
- Eligible blocks (age class >= 40): 221572
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 8.37 MB
- Schedules: 0.26 MB
- Runs: 0.00 MB
- Total: 8.63 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
