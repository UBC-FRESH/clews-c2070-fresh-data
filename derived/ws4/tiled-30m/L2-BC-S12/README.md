# WS4 tiled 30-m dataset — L2|BC|S12

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `L2|BC|S12` (parent `L2|BC`)
- Tile / row / col: `L2` / 1 / 2
- Province: `BC`
- Centroid: 54.852157, -130.413485
- Allocated harvest: 2563.683516 m3
- Productive subcell area: 3118.139003 ha
- Committed geometry area: 5215.719023 ha
- Clipped inventory geometry: 5215.719023 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 56617
- Blocks: 32185
- Forest area: 5095.53 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 3210
- Scheduled area: 497.61 ha
- Eligible blocks (age class >= 40): 32097
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 1.12 MB
- Schedules: 0.03 MB
- Runs: 0.00 MB
- Total: 1.16 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
