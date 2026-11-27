# WS4 tiled 30-m dataset — E16|MB|S21

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `E16|MB|S21` (parent `E16|MB`)
- Tile / row / col: `E16` / 2 / 1
- Province: `MB`
- Centroid: 51.463713, -96.247278
- Allocated harvest: 8452.232755 m3
- Productive subcell area: 188650.391981 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1950590
- Blocks: 832580
- Forest area: 175553.10 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 74334
- Scheduled area: 14461.74 ha
- Eligible blocks (age class >= 40): 743338
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 25.24 MB
- Schedules: 0.88 MB
- Runs: 0.00 MB
- Total: 26.13 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
