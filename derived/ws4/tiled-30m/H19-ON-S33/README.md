# WS4 tiled 30-m dataset — H19|ON|S33

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `H19|ON|S33` (parent `H19|ON`)
- Tile / row / col: `H19` / 3 / 3
- Province: `ON`
- Centroid: 55.768657, -87.445675
- Allocated harvest: 5951.996096 m3
- Productive subcell area: 108490.617920 ha
- Committed geometry area: 234767.137347 ha
- Clipped inventory geometry: 234767.137347 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1410223
- Blocks: 589936
- Forest area: 126920.07 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 51365
- Scheduled area: 11503.80 ha
- Eligible blocks (age class >= 40): 513650
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 18.59 MB
- Schedules: 0.61 MB
- Runs: 0.00 MB
- Total: 19.20 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
