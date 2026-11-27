# WS4 tiled 30-m dataset — J10|AB|S32

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `J10|AB|S32` (parent `J10|AB`)
- Tile / row / col: `J10` / 3 / 2
- Province: `AB`
- Centroid: 57.686163, -111.262099
- Allocated harvest: 63505.985473 m3
- Productive subcell area: 216383.211414 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2483128
- Blocks: 555747
- Forest area: 223481.52 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 44619
- Scheduled area: 9881.01 ha
- Eligible blocks (age class >= 40): 446182
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 23.79 MB
- Schedules: 0.53 MB
- Runs: 0.00 MB
- Total: 24.32 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
