# WS4 tiled 30-m dataset — H13|SK|S21

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `H13|SK|S21` (parent `H13|SK`)
- Tile / row / col: `H13` / 2 / 1
- Province: `SK`
- Centroid: 55.242519, -103.619275
- Allocated harvest: 32942.635155 m3
- Productive subcell area: 180395.801396 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1770919
- Blocks: 452659
- Forest area: 159382.71 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 33795
- Scheduled area: 6420.24 ha
- Eligible blocks (age class >= 40): 337944
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 18.27 MB
- Schedules: 0.40 MB
- Runs: 0.00 MB
- Total: 18.67 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
