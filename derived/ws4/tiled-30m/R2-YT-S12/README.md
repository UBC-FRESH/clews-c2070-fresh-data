# WS4 tiled 30-m dataset — R2|YT|S12

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `R2|YT|S12` (parent `R2|YT`)
- Tile / row / col: `R2` / 1 / 2
- Province: `YT`
- Centroid: 61.630919, -140.216743
- Allocated harvest: 271.575405 m3
- Productive subcell area: 128839.581913 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1158839
- Blocks: 486186
- Forest area: 104295.51 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 39871
- Scheduled area: 8986.95 ha
- Eligible blocks (age class >= 40): 398702
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 15.45 MB
- Schedules: 0.47 MB
- Runs: 0.00 MB
- Total: 15.92 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
