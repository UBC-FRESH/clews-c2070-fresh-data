# WS4 tiled 30-m dataset — E6|BC|S33

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `E6|BC|S33` (parent `E6|BC`)
- Tile / row / col: `E6` / 3 / 3
- Province: `BC`
- Centroid: 49.682567, -116.024162
- Allocated harvest: 191461.677037 m3
- Productive subcell area: 207791.088770 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2115874
- Blocks: 1017693
- Forest area: 190428.66 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 89864
- Scheduled area: 14537.61 ha
- Eligible blocks (age class >= 40): 898638
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 28.95 MB
- Schedules: 1.07 MB
- Runs: 0.00 MB
- Total: 30.02 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
