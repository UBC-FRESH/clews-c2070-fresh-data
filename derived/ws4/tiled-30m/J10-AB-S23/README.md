# WS4 tiled 30-m dataset — J10|AB|S23

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `J10|AB|S23` (parent `J10|AB`)
- Tile / row / col: `J10` / 2 / 3
- Province: `AB`
- Centroid: 57.352149, -110.321200
- Allocated harvest: 48902.380517 m3
- Productive subcell area: 166624.516780 ha
- Committed geometry area: 192510.911188 ha
- Clipped inventory geometry: 192510.911188 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1816958
- Blocks: 324932
- Forest area: 163526.22 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 21168
- Scheduled area: 5505.84 ha
- Eligible blocks (age class >= 40): 211671
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 16.34 MB
- Schedules: 0.25 MB
- Runs: 0.00 MB
- Total: 16.59 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
