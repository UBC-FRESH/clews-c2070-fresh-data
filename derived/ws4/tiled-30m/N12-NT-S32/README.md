# WS4 tiled 30-m dataset — N12|NT|S32

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `N12|NT|S32` (parent `N12|NT`)
- Tile / row / col: `N12` / 3 / 2
- Province: `NT`
- Centroid: 63.719652, -108.370224
- Allocated harvest: 17.062886 m3
- Productive subcell area: 34698.322056 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 39234
- Blocks: 34801
- Forest area: 3531.06 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 1305
- Scheduled area: 127.89 ha
- Eligible blocks (age class >= 40): 13046
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 1.02 MB
- Schedules: 0.01 MB
- Runs: 0.00 MB
- Total: 1.04 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
