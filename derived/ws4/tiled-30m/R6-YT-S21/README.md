# WS4 tiled 30-m dataset — R6|YT|S21

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `R6|YT|S21` (parent `R6|YT`)
- Tile / row / col: `R6` / 2 / 1
- Province: `YT`
- Centroid: 65.053976, -132.380556
- Allocated harvest: 0.677299 m3
- Productive subcell area: 583.729042 ha
- Committed geometry area: 1294.348917 ha
- Clipped inventory geometry: 1294.348917 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 92
- Blocks: 81
- Forest area: 8.28 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 0
- Scheduled area: 0.00 ha
- Eligible blocks (age class >= 40): 0
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 0.08 MB
- Schedules: 0.00 MB
- Runs: 0.00 MB
- Total: 0.08 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
