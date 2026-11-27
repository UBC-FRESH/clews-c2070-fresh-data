# WS4 tiled 30-m dataset — I30|NL|S31

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `I30|NL|S31` (parent `I30|NL`)
- Tile / row / col: `I30` / 3 / 1
- Province: `NL`
- Centroid: 52.765252, -63.456513
- Allocated harvest: 9522.985774 m3
- Productive subcell area: 145253.598734 ha
- Committed geometry area: 197047.348627 ha
- Clipped inventory geometry: 197047.348627 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1696081
- Blocks: 479149
- Forest area: 152647.29 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 43686
- Scheduled area: 15608.61 ha
- Eligible blocks (age class >= 40): 436860
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 19.07 MB
- Schedules: 0.51 MB
- Runs: 0.00 MB
- Total: 19.58 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
