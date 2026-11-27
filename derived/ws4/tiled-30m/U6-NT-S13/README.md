# WS4 tiled 30-m dataset — U6|NT|S13

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `U6|NT|S13` (parent `U6|NT`)
- Tile / row / col: `U6` / 1 / 3
- Province: `NT`
- Centroid: 68.625805, -135.168045
- Allocated harvest: 65.341848 m3
- Productive subcell area: 55130.502413 ha
- Committed geometry area: 237453.103505 ha
- Clipped inventory geometry: 237453.103505 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1094855
- Blocks: 632928
- Forest area: 98536.95 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 53335
- Scheduled area: 8011.26 ha
- Eligible blocks (age class >= 40): 533345
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 16.65 MB
- Schedules: 0.63 MB
- Runs: 0.00 MB
- Total: 17.28 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
