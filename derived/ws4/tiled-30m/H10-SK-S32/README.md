# WS4 tiled 30-m dataset — H10|SK|S32

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `H10|SK|S32` (parent `H10|SK`)
- Tile / row / col: `H10` / 3 / 2
- Province: `SK`
- Centroid: 55.022949, -109.830119
- Allocated harvest: 20857.369980 m3
- Productive subcell area: 81118.757374 ha
- Committed geometry area: 108844.450749 ha
- Clipped inventory geometry: 108844.450749 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 751078
- Blocks: 244096
- Forest area: 67597.02 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 19901
- Scheduled area: 6144.66 ha
- Eligible blocks (age class >= 40): 199007
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 8.90 MB
- Schedules: 0.23 MB
- Runs: 0.00 MB
- Total: 9.13 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
