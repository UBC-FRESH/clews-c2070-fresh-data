# WS4 tiled 30-m dataset — M4|BC|S12

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `M4|BC|S12` (parent `M4|BC`)
- Tile / row / col: `M4` / 1 / 2
- Province: `BC`
- Centroid: 57.548696, -127.870694
- Allocated harvest: 93682.180011 m3
- Productive subcell area: 139942.345505 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1584434
- Blocks: 766849
- Forest area: 142599.06 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 68147
- Scheduled area: 11257.83 ha
- Eligible blocks (age class >= 40): 681466
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 21.84 MB
- Schedules: 0.81 MB
- Runs: 0.00 MB
- Total: 22.65 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
