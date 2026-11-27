# WS4 tiled 30-m dataset — I16|MB|S21

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `I16|MB|S21` (parent `I16|MB`)
- Tile / row / col: `I16` / 2 / 1
- Province: `MB`
- Centroid: 56.943980, -96.445168
- Allocated harvest: 3456.593616 m3
- Productive subcell area: 133820.004351 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1526298
- Blocks: 452907
- Forest area: 137366.82 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 27828
- Scheduled area: 7496.46 ha
- Eligible blocks (age class >= 40): 278271
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 17.24 MB
- Schedules: 0.33 MB
- Runs: 0.00 MB
- Total: 17.57 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
