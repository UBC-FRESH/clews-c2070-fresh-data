# WS4 tiled 30-m dataset — I30|NL|S23

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `I30|NL|S23` (parent `I30|NL`)
- Tile / row / col: `I30` / 2 / 3
- Province: `NL`
- Centroid: 52.073604, -62.559384
- Allocated harvest: 3565.274895 m3
- Productive subcell area: 54380.949553 ha
- Committed geometry area: 73771.817144 ha
- Clipped inventory geometry: 73771.817144 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 692010
- Blocks: 179887
- Forest area: 62280.90 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 17278
- Scheduled area: 3848.94 ha
- Eligible blocks (age class >= 40): 172773
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 7.62 MB
- Schedules: 0.20 MB
- Runs: 0.00 MB
- Total: 7.82 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
