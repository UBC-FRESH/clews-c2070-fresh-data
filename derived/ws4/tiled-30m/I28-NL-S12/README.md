# WS4 tiled 30-m dataset — I28|NL|S12

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `I28|NL|S12` (parent `I28|NL`)
- Tile / row / col: `I28` / 1 / 2
- Province: `NL`
- Centroid: 53.010152, -67.240079
- Allocated harvest: 1006.735927 m3
- Productive subcell area: 22640.445392 ha
- Committed geometry area: 42537.213001 ha
- Clipped inventory geometry: 42537.213001 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 240694
- Blocks: 104062
- Forest area: 21662.46 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 7955
- Scheduled area: 1581.39 ha
- Eligible blocks (age class >= 40): 79550
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 3.85 MB
- Schedules: 0.09 MB
- Runs: 0.00 MB
- Total: 3.94 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
