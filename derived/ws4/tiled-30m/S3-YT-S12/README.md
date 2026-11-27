# WS4 tiled 30-m dataset — S3|YT|S12

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `S3|YT|S12` (parent `S3|YT`)
- Tile / row / col: `S3` / 1 / 2
- Province: `YT`
- Centroid: 63.587474, -139.888694
- Allocated harvest: 472.705010 m3
- Productive subcell area: 194978.868526 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2413213
- Blocks: 701757
- Forest area: 217189.17 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 62187
- Scheduled area: 16068.24 ha
- Eligible blocks (age class >= 40): 621865
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 26.32 MB
- Schedules: 0.74 MB
- Runs: 0.00 MB
- Total: 27.06 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
