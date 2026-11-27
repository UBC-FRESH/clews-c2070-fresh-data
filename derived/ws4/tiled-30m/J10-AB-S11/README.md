# WS4 tiled 30-m dataset — J10|AB|S11

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `J10|AB|S11` (parent `J10|AB`)
- Tile / row / col: `J10` / 1 / 1
- Province: `AB`
- Centroid: 56.679415, -111.647473
- Allocated harvest: 63505.985473 m3
- Productive subcell area: 216383.211414 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2233270
- Blocks: 783602
- Forest area: 200994.30 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 56232
- Scheduled area: 11463.66 ha
- Eligible blocks (age class >= 40): 562320
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 26.71 MB
- Schedules: 0.67 MB
- Runs: 0.00 MB
- Total: 27.37 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
