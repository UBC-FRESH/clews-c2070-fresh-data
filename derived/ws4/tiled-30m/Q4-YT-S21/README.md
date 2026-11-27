# WS4 tiled 30-m dataset — Q4|YT|S21

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `Q4|YT|S21` (parent `Q4|YT`)
- Tile / row / col: `Q4` / 2 / 1
- Province: `YT`
- Centroid: 62.344763, -135.142784
- Allocated harvest: 327.910389 m3
- Productive subcell area: 191647.548919 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2385633
- Blocks: 870278
- Forest area: 214706.97 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 75198
- Scheduled area: 17806.14 ha
- Eligible blocks (age class >= 40): 751975
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 28.78 MB
- Schedules: 0.89 MB
- Runs: 0.00 MB
- Total: 29.68 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
