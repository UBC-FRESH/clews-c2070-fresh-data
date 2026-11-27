# WS4 tiled 30-m dataset — N4|BC|S13

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `N4|BC|S13` (parent `N4|BC`)
- Tile / row / col: `N4` / 1 / 3
- Province: `BC`
- Centroid: 58.976617, -128.418068
- Allocated harvest: 44279.454431 m3
- Productive subcell area: 151492.572394 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1618744
- Blocks: 844682
- Forest area: 145686.96 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 77146
- Scheduled area: 12173.40 ha
- Eligible blocks (age class >= 40): 771458
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 23.28 MB
- Schedules: 0.92 MB
- Runs: 0.00 MB
- Total: 24.19 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
