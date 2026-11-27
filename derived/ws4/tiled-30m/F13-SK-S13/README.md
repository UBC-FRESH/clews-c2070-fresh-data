# WS4 tiled 30-m dataset — F13|SK|S13

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `F13|SK|S13` (parent `F13|SK`)
- Tile / row / col: `F13` / 1 / 3
- Province: `SK`
- Centroid: 52.168999, -101.718144
- Allocated harvest: 12715.916702 m3
- Productive subcell area: 51351.683965 ha
- Committed geometry area: 71583.077293 ha
- Clipped inventory geometry: 71583.077293 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 439727
- Blocks: 130785
- Forest area: 39575.43 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 11799
- Scheduled area: 3960.63 ha
- Eligible blocks (age class >= 40): 117985
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 5.58 MB
- Schedules: 0.13 MB
- Runs: 0.00 MB
- Total: 5.71 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
