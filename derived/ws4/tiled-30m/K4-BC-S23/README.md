# WS4 tiled 30-m dataset — K4|BC|S23

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `K4|BC|S23` (parent `K4|BC`)
- Tile / row / col: `K4` / 2 / 3
- Province: `BC`
- Centroid: 55.745923, -125.154681
- Allocated harvest: 84412.572477 m3
- Productive subcell area: 216445.726840 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2493317
- Blocks: 929040
- Forest area: 224398.53 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 86583
- Scheduled area: 16471.98 ha
- Eligible blocks (age class >= 40): 865829
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 30.52 MB
- Schedules: 1.03 MB
- Runs: 0.00 MB
- Total: 31.55 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
