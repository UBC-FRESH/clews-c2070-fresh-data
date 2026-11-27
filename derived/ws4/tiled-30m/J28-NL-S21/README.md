# WS4 tiled 30-m dataset — J28|NL|S21

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `J28|NL|S21` (parent `J28|NL`)
- Tile / row / col: `J28` / 2 / 1
- Province: `NL`
- Centroid: 54.753376, -66.871906
- Allocated harvest: 2801.835523 m3
- Productive subcell area: 68447.600446 ha
- Committed geometry area: 135991.415117 ha
- Clipped inventory geometry: 135991.415117 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 829131
- Blocks: 471546
- Forest area: 74621.79 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 41537
- Scheduled area: 6481.44 ha
- Eligible blocks (age class >= 40): 415362
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 12.55 MB
- Schedules: 0.49 MB
- Runs: 0.00 MB
- Total: 13.04 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
