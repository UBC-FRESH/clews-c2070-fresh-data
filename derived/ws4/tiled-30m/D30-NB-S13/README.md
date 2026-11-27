# WS4 tiled 30-m dataset — D30|NB|S13

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `D30|NB|S13` (parent `D30|NB`)
- Tile / row / col: `D30` / 1 / 3
- Province: `NB`
- Centroid: 45.543408, -67.380639
- Allocated harvest: 115484.006871 m3
- Productive subcell area: 119658.630318 ha
- Committed geometry area: 136754.327212 ha
- Clipped inventory geometry: 136754.327212 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1408503
- Blocks: 567467
- Forest area: 126765.27 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 50386
- Scheduled area: 9780.75 ha
- Eligible blocks (age class >= 40): 503851
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 18.20 MB
- Schedules: 0.60 MB
- Runs: 0.00 MB
- Total: 18.80 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
