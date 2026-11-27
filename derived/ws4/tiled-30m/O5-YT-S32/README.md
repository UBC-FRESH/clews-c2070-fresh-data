# WS4 tiled 30-m dataset — O5|YT|S32

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `O5|YT|S32` (parent `O5|YT`)
- Tile / row / col: `O5` / 3 / 2
- Province: `YT`
- Centroid: 61.435169, -129.168619
- Allocated harvest: 258.538255 m3
- Productive subcell area: 172813.327718 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1855638
- Blocks: 816652
- Forest area: 167007.42 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 74567
- Scheduled area: 14750.10 ha
- Eligible blocks (age class >= 40): 745670
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 24.61 MB
- Schedules: 0.88 MB
- Runs: 0.00 MB
- Total: 25.50 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
