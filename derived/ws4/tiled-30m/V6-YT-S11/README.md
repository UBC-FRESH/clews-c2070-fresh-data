# WS4 tiled 30-m dataset — V6|YT|S11

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `V6|YT|S11` (parent `V6|YT`)
- Tile / row / col: `V6` / 1 / 1
- Province: `YT`
- Centroid: 69.149082, -139.563144
- Allocated harvest: 12.579901 m3
- Productive subcell area: 10896.148460 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 86275
- Blocks: 48072
- Forest area: 7764.75 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 1466
- Scheduled area: 220.14 ha
- Eligible blocks (age class >= 40): 14660
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 1.67 MB
- Schedules: 0.02 MB
- Runs: 0.00 MB
- Total: 1.68 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
