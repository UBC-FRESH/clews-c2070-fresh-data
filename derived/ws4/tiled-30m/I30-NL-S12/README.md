# WS4 tiled 30-m dataset — I30|NL|S12

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `I30|NL|S12` (parent `I30|NL`)
- Tile / row / col: `I30` / 1 / 2
- Province: `NL`
- Centroid: 52.013209, -63.678789
- Allocated harvest: 153.336851 m3
- Productive subcell area: 2338.838890 ha
- Committed geometry area: 3172.809529 ha
- Clipped inventory geometry: 3172.809529 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 24841
- Blocks: 11725
- Forest area: 2235.69 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 1143
- Scheduled area: 224.64 ha
- Eligible blocks (age class >= 40): 11426
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 0.48 MB
- Schedules: 0.01 MB
- Runs: 0.00 MB
- Total: 0.49 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
