# WS4 tiled 30-m dataset — D22|ON|S21

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `D22|ON|S21` (parent `D22|ON`)
- Tile / row / col: `D22` / 2 / 1
- Province: `ON`
- Centroid: 49.459766, -83.691309
- Allocated harvest: 49456.255781 m3
- Productive subcell area: 231072.091541 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2610620
- Blocks: 873718
- Forest area: 234955.80 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 81574
- Scheduled area: 20054.70 ha
- Eligible blocks (age class >= 40): 815734
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 31.11 MB
- Schedules: 0.97 MB
- Runs: 0.00 MB
- Total: 32.08 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
