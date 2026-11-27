# WS4 tiled 30-m dataset — R10|NT|S11

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `R10|NT|S11` (parent `R10|NT`)
- Tile / row / col: `R10` / 1 / 1
- Province: `NT`
- Centroid: 67.169701, -119.148946
- Allocated harvest: 1.902750 m3
- Productive subcell area: 5434.371216 ha
- Committed geometry area: 185634.228043 ha
- Clipped inventory geometry: 185634.228043 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 316310
- Blocks: 169345
- Forest area: 28467.90 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 8014
- Scheduled area: 1300.59 ha
- Eligible blocks (age class >= 40): 80140
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 5.29 MB
- Schedules: 0.09 MB
- Runs: 0.00 MB
- Total: 5.39 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
