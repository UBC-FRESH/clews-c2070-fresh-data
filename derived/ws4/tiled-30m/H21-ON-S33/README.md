# WS4 tiled 30-m dataset — H21|ON|S33

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `H21|ON|S33` (parent `H21|ON`)
- Tile / row / col: `H21` / 3 / 3
- Province: `ON`
- Centroid: 55.193878, -82.995851
- Allocated harvest: 247.422242 m3
- Productive subcell area: 4568.594831 ha
- Committed geometry area: 14973.941796 ha
- Clipped inventory geometry: 14973.941796 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 5882
- Blocks: 4286
- Forest area: 529.38 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 1472
- Scheduled area: 167.13 ha
- Eligible blocks (age class >= 40): 1472
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 0.19 MB
- Schedules: 0.01 MB
- Runs: 0.00 MB
- Total: 0.20 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
