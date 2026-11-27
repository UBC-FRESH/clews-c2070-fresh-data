# WS4 tiled 30-m dataset — K28|NL|S33

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `K28|NL|S33` (parent `K28|NL`)
- Tile / row / col: `K28` / 3 / 3
- Province: `NL`
- Centroid: 56.109789, -63.784241
- Allocated harvest: 291.666034 m3
- Productive subcell area: 7811.055457 ha
- Committed geometry area: 45689.157625 ha
- Clipped inventory geometry: 45689.157625 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 52183
- Blocks: 26351
- Forest area: 4696.47 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 1344
- Scheduled area: 198.18 ha
- Eligible blocks (age class >= 40): 13436
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 0.98 MB
- Schedules: 0.01 MB
- Runs: 0.00 MB
- Total: 0.99 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
