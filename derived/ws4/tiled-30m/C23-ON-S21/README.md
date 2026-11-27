# WS4 tiled 30-m dataset — C23|ON|S21

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `C23|ON|S21` (parent `C23|ON`)
- Tile / row / col: `C23` / 2 / 1
- Province: `ON`
- Centroid: 47.881860, -82.079191
- Allocated harvest: 60746.402306 m3
- Productive subcell area: 219318.652196 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2341647
- Blocks: 762358
- Forest area: 210748.23 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 63816
- Scheduled area: 14605.11 ha
- Eligible blocks (age class >= 40): 638155
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 27.89 MB
- Schedules: 0.76 MB
- Runs: 0.00 MB
- Total: 28.64 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
