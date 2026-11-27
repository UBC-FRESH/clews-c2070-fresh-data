# WS4 tiled 30-m dataset — J32|NL|S11

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `J32|NL|S11` (parent `J32|NL`)
- Tile / row / col: `J32` / 1 / 1
- Province: `NL`
- Centroid: 52.026943, -59.370075
- Allocated harvest: 441.328890 m3
- Productive subcell area: 7536.790174 ha
- Committed geometry area: 9658.606904 ha
- Clipped inventory geometry: 9658.606904 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 98330
- Blocks: 26567
- Forest area: 8849.70 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 2498
- Scheduled area: 715.59 ha
- Eligible blocks (age class >= 40): 24980
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 1.38 MB
- Schedules: 0.03 MB
- Runs: 0.00 MB
- Total: 1.41 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
