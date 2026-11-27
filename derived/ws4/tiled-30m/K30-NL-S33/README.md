# WS4 tiled 30-m dataset — K30|NL|S33

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `K30|NL|S33` (parent `K30|NL`)
- Tile / row / col: `K30` / 3 / 3
- Province: `NL`
- Centroid: 54.665269, -59.871588
- Allocated harvest: 9866.063414 m3
- Productive subcell area: 161564.542628 ha
- Committed geometry area: 245292.063431 ha
- Clipped inventory geometry: 245292.063431 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1856777
- Blocks: 528333
- Forest area: 167109.93 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 46591
- Scheduled area: 15358.23 ha
- Eligible blocks (age class >= 40): 465904
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 20.64 MB
- Schedules: 0.55 MB
- Runs: 0.00 MB
- Total: 21.19 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
