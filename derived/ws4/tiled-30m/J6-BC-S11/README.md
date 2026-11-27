# WS4 tiled 30-m dataset — J6|BC|S11

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `J6|BC|S11` (parent `J6|BC`)
- Tile / row / col: `J6` / 1 / 1
- Province: `BC`
- Centroid: 54.869146, -120.878209
- Allocated harvest: 118034.013691 m3
- Productive subcell area: 209725.032340 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2592641
- Blocks: 1122701
- Forest area: 233337.69 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 105746
- Scheduled area: 19283.49 ha
- Eligible blocks (age class >= 40): 1057455
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 34.57 MB
- Schedules: 1.27 MB
- Runs: 0.00 MB
- Total: 35.84 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
