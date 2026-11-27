# WS4 tiled 30-m dataset — L28|NL|S32

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `L28|NL|S32` (parent `L28|NL`)
- Tile / row / col: `L28` / 3 / 2
- Province: `NL`
- Centroid: 57.453648, -63.491840
- Allocated harvest: 929.552762 m3
- Productive subcell area: 18417.950321 ha
- Committed geometry area: 170950.832957 ha
- Clipped inventory geometry: 170950.832957 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 10706
- Blocks: 6684
- Forest area: 963.54 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 3114
- Scheduled area: 518.13 ha
- Eligible blocks (age class >= 40): 3114
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 0.28 MB
- Schedules: 0.03 MB
- Runs: 0.00 MB
- Total: 0.31 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
