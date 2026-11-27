# WS4 tiled 30-m dataset — I17|MB|S32

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `I17|MB|S32` (parent `I17|MB`)
- Tile / row / col: `I17` / 3 / 2
- Province: `MB`
- Centroid: 57.396763, -93.055361
- Allocated harvest: 1709.562505 m3
- Productive subcell area: 124286.482604 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 491005
- Blocks: 251130
- Forest area: 44190.45 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 17968
- Scheduled area: 3196.89 ha
- Eligible blocks (age class >= 40): 179675
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 7.49 MB
- Schedules: 0.21 MB
- Runs: 0.00 MB
- Total: 7.70 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
