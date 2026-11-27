# WS4 tiled 30-m dataset — F23|ON|S21

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `F23|ON|S21` (parent `F23|ON`)
- Tile / row / col: `F23` / 2 / 1
- Province: `ON`
- Centroid: 51.768876, -80.889017
- Allocated harvest: 5071.159921 m3
- Productive subcell area: 77076.187448 ha
- Committed geometry area: 112326.449940 ha
- Clipped inventory geometry: 112326.449940 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 488858
- Blocks: 268690
- Forest area: 43997.22 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 25067
- Scheduled area: 4134.33 ha
- Eligible blocks (age class >= 40): 250664
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 7.81 MB
- Schedules: 0.29 MB
- Runs: 0.00 MB
- Total: 8.10 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
