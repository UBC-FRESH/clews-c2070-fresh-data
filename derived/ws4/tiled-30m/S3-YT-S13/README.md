# WS4 tiled 30-m dataset — S3|YT|S13

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `S3|YT|S13` (parent `S3|YT`)
- Tile / row / col: `S3` / 1 / 3
- Province: `YT`
- Centroid: 63.885334, -139.089698
- Allocated harvest: 472.705010 m3
- Productive subcell area: 194978.868526 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2385568
- Blocks: 763279
- Forest area: 214701.12 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 68771
- Scheduled area: 15868.53 ha
- Eligible blocks (age class >= 40): 687705
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 27.60 MB
- Schedules: 0.81 MB
- Runs: 0.00 MB
- Total: 28.42 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
