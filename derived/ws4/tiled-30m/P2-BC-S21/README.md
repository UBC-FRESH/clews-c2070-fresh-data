# WS4 tiled 30-m dataset — P2|BC|S21

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `P2|BC|S21` (parent `P2|BC`)
- Tile / row / col: `P2` / 2 / 1
- Province: `BC`
- Centroid: 59.602818, -137.845486
- Allocated harvest: 6857.709692 m3
- Productive subcell area: 21187.458068 ha
- Committed geometry area: 179678.208672 ha
- Clipped inventory geometry: 179678.208672 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 355520
- Blocks: 149395
- Forest area: 31996.80 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 12628
- Scheduled area: 2572.74 ha
- Eligible blocks (age class >= 40): 126276
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 5.37 MB
- Schedules: 0.14 MB
- Runs: 0.00 MB
- Total: 5.51 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
