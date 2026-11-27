# WS4 tiled 30-m dataset — C21|ON|S13

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `C21|ON|S13` (parent `C21|ON`)
- Tile / row / col: `C21` / 1 / 3
- Province: `ON`
- Centroid: 47.760050, -84.729674
- Allocated harvest: 46825.228171 m3
- Productive subcell area: 163548.492977 ha
- Committed geometry area: 181878.563445 ha
- Clipped inventory geometry: 181878.563445 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1850145
- Blocks: 528490
- Forest area: 166513.05 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 51161
- Scheduled area: 15561.27 ha
- Eligible blocks (age class >= 40): 511608
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 20.96 MB
- Schedules: 0.60 MB
- Runs: 0.00 MB
- Total: 21.56 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
