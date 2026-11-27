# WS4 tiled 30-m dataset — Q7|NT|S22

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `Q7|NT|S22` (parent `Q7|NT`)
- Tile / row / col: `Q7` / 2 / 2
- Province: `NT`
- Centroid: 64.815795, -126.348795
- Allocated harvest: 140.807692 m3
- Productive subcell area: 144411.735102 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1808342
- Blocks: 531543
- Forest area: 162750.78 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 40527
- Scheduled area: 9132.66 ha
- Eligible blocks (age class >= 40): 405262
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 19.66 MB
- Schedules: 0.48 MB
- Runs: 0.00 MB
- Total: 20.14 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
