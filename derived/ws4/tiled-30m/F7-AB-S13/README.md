# WS4 tiled 30-m dataset — F7|AB|S13

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `F7|AB|S13` (parent `F7|AB`)
- Tile / row / col: `F7` / 1 / 3
- Province: `AB`
- Centroid: 50.533108, -114.241587
- Allocated harvest: 124459.651060 m3
- Productive subcell area: 142285.085300 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1054282
- Blocks: 432416
- Forest area: 94885.38 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 37164
- Scheduled area: 10207.44 ha
- Eligible blocks (age class >= 40): 371631
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 13.75 MB
- Schedules: 0.44 MB
- Runs: 0.00 MB
- Total: 14.19 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
