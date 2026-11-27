# WS4 tiled 30-m dataset — H21|ON|S21

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `H21|ON|S21` (parent `H21|ON`)
- Tile / row / col: `H21` / 2 / 1
- Province: `ON`
- Centroid: 55.046636, -84.341952
- Allocated harvest: 3794.682936 m3
- Productive subcell area: 70067.948234 ha
- Committed geometry area: 229653.409299 ha
- Clipped inventory geometry: 229653.409299 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 671708
- Blocks: 322918
- Forest area: 60453.72 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 25098
- Scheduled area: 4981.68 ha
- Eligible blocks (age class >= 40): 250972
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 9.69 MB
- Schedules: 0.29 MB
- Runs: 0.00 MB
- Total: 9.99 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
