# WS4 tiled 30-m dataset — P5|YT|S12

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `P5|YT|S12` (parent `P5|YT`)
- Tile / row / col: `P5` / 1 / 2
- Province: `YT`
- Centroid: 61.831457, -129.669112
- Allocated harvest: 178.544340 m3
- Productive subcell area: 176847.291549 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2035750
- Blocks: 909775
- Forest area: 183217.50 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 83102
- Scheduled area: 16558.65 ha
- Eligible blocks (age class >= 40): 831020
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 27.19 MB
- Schedules: 0.99 MB
- Runs: 0.00 MB
- Total: 28.17 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
