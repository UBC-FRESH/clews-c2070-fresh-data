# WS4 tiled 30-m dataset — B26|QC|S23

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `B26|QC|S23` (parent `B26|QC`)
- Tile / row / col: `B26` / 2 / 3
- Province: `QC`
- Centroid: 45.509016, -75.755214
- Allocated harvest: 31001.461863 m3
- Productive subcell area: 51409.601969 ha
- Committed geometry area: 63858.780156 ha
- Clipped inventory geometry: 63858.780156 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 384502
- Blocks: 136689
- Forest area: 34605.18 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 11220
- Scheduled area: 3199.14 ha
- Eligible blocks (age class >= 40): 112196
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 5.48 MB
- Schedules: 0.13 MB
- Runs: 0.00 MB
- Total: 5.60 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
