# WS4 tiled 30-m dataset — J32|NL|S32

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `J32|NL|S32` (parent `J32|NL`)
- Tile / row / col: `J32` / 3 / 2
- Province: `NL`
- Centroid: 52.288956, -57.882537
- Allocated harvest: 11388.021164 m3
- Productive subcell area: 194478.829652 ha
- Committed geometry area: 249230.046658 ha
- Clipped inventory geometry: 249230.046658 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2246101
- Blocks: 965608
- Forest area: 202149.09 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 90262
- Scheduled area: 18996.57 ha
- Eligible blocks (age class >= 40): 902611
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 29.56 MB
- Schedules: 1.07 MB
- Runs: 0.00 MB
- Total: 30.63 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
