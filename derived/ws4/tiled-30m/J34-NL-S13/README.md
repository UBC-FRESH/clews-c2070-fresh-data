# WS4 tiled 30-m dataset — J34|NL|S13

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `J34|NL|S13` (parent `J34|NL`)
- Tile / row / col: `J34` / 1 / 3
- Province: `NL`
- Centroid: 49.581999, -54.634511
- Allocated harvest: 1697.569611 m3
- Productive subcell area: 29183.673755 ha
- Committed geometry area: 36637.764974 ha
- Clipped inventory geometry: 36637.764974 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 300812
- Blocks: 183544
- Forest area: 27073.08 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 16418
- Scheduled area: 2415.60 ha
- Eligible blocks (age class >= 40): 164172
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 5.49 MB
- Schedules: 0.19 MB
- Runs: 0.00 MB
- Total: 5.68 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
