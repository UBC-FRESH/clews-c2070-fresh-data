# WS4 tiled 30-m dataset — M25|QC|S13

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `M25|QC|S13` (parent `M25|QC`)
- Tile / row / col: `M25` / 1 / 3
- Province: `QC`
- Centroid: 59.459544, -69.757617
- Allocated harvest: 3.174053 m3
- Productive subcell area: 24.801285 ha
- Committed geometry area: 134440.105970 ha
- Clipped inventory geometry: 134440.105970 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1079
- Blocks: 967
- Forest area: 97.11 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 24
- Scheduled area: 2.16 ha
- Eligible blocks (age class >= 40): 24
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 0.09 MB
- Schedules: 0.00 MB
- Runs: 0.00 MB
- Total: 0.09 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
