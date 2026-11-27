# WS4 tiled 30-m dataset — M5|BC|S21

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `M5|BC|S21` (parent `M5|BC`)
- Tile / row / col: `M5` / 2 / 1
- Province: `BC`
- Centroid: 58.399131, -126.778123
- Allocated harvest: 44439.105201 m3
- Productive subcell area: 135935.973745 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1995991
- Blocks: 972612
- Forest area: 179639.19 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 90875
- Scheduled area: 15914.43 ha
- Eligible blocks (age class >= 40): 908744
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 27.55 MB
- Schedules: 1.08 MB
- Runs: 0.00 MB
- Total: 28.63 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
