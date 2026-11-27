# WS4 tiled 30-m dataset — Q6|NT|S13

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `Q6|NT|S13` (parent `Q6|NT`)
- Tile / row / col: `Q6` / 1 / 3
- Province: `NT`
- Centroid: 63.964092, -127.705598
- Allocated harvest: 25.707972 m3
- Productive subcell area: 42534.431928 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 768445
- Blocks: 376306
- Forest area: 69160.05 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 28319
- Scheduled area: 5283.45 ha
- Eligible blocks (age class >= 40): 283182
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 11.05 MB
- Schedules: 0.33 MB
- Runs: 0.00 MB
- Total: 11.38 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
