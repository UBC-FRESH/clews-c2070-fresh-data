# WS4 tiled 30-m dataset — C17|ON|S21

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `C17|ON|S21` (parent `C17|ON`)
- Tile / row / col: `C17` / 2 / 1
- Province: `ON`
- Centroid: 48.819435, -94.109093
- Allocated harvest: 30666.936372 m3
- Productive subcell area: 138990.790886 ha
- Committed geometry area: 180273.356910 ha
- Clipped inventory geometry: 180273.356910 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1594055
- Blocks: 522287
- Forest area: 143464.95 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 42820
- Scheduled area: 11449.44 ha
- Eligible blocks (age class >= 40): 428196
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 19.20 MB
- Schedules: 0.50 MB
- Runs: 0.00 MB
- Total: 19.70 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
