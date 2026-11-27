# WS4 tiled 30-m dataset — N6|YT|S31

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `N6|YT|S31` (parent `N6|YT`)
- Tile / row / col: `N6` / 3 / 1
- Province: `YT`
- Centroid: 60.634916, -126.080417
- Allocated harvest: 407.289097 m3
- Productive subcell area: 171508.520743 ha
- Committed geometry area: 198107.655517 ha
- Clipped inventory geometry: 198107.655517 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1776307
- Blocks: 773895
- Forest area: 159867.63 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 68223
- Scheduled area: 12216.60 ha
- Eligible blocks (age class >= 40): 682230
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 23.21 MB
- Schedules: 0.81 MB
- Runs: 0.00 MB
- Total: 24.02 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
