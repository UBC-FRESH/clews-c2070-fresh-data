# WS4 tiled 30-m dataset — M9|AB|S11

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `M9|AB|S11` (parent `M9|AB`)
- Tile / row / col: `M9` / 1 / 1
- Province: `AB`
- Centroid: 59.980466, -116.689361
- Allocated harvest: 1954.040924 m3
- Productive subcell area: 5168.732622 ha
- Committed geometry area: 6659.465317 ha
- Clipped inventory geometry: 6659.465317 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 50442
- Blocks: 24275
- Forest area: 4539.78 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 2221
- Scheduled area: 390.87 ha
- Eligible blocks (age class >= 40): 22210
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 0.95 MB
- Schedules: 0.02 MB
- Runs: 0.00 MB
- Total: 0.97 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
