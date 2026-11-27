# WS4 tiled 30-m dataset — B27|ON|S21

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `B27|ON|S21` (parent `B27|ON`)
- Tile / row / col: `B27` / 2 / 1
- Province: `ON`
- Centroid: 45.229016, -75.086982
- Allocated harvest: 13772.642856 m3
- Productive subcell area: 41495.608902 ha
- Committed geometry area: 243347.258934 ha
- Clipped inventory geometry: 243347.258934 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1280581
- Blocks: 365183
- Forest area: 115252.29 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 25908
- Scheduled area: 7879.95 ha
- Eligible blocks (age class >= 40): 259073
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 14.65 MB
- Schedules: 0.30 MB
- Runs: 0.00 MB
- Total: 14.95 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
