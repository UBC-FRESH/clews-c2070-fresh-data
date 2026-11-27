# WS4 tiled 30-m dataset — J28|NL|S33

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `J28|NL|S33` (parent `J28|NL`)
- Tile / row / col: `J28` / 3 / 3
- Province: `NL`
- Centroid: 54.734708, -65.139533
- Allocated harvest: 3056.127437 m3
- Productive subcell area: 74659.839240 ha
- Committed geometry area: 148333.865970 ha
- Clipped inventory geometry: 148333.865970 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1105785
- Blocks: 589339
- Forest area: 99520.65 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 55156
- Scheduled area: 9138.87 ha
- Eligible blocks (age class >= 40): 551558
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 15.99 MB
- Schedules: 0.65 MB
- Runs: 0.00 MB
- Total: 16.64 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
