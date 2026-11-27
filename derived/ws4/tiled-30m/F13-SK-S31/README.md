# WS4 tiled 30-m dataset — F13|SK|S31

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `F13|SK|S31` (parent `F13|SK`)
- Tile / row / col: `F13` / 3 / 1
- Province: `SK`
- Centroid: 52.978227, -103.109575
- Allocated harvest: 44409.646743 m3
- Productive subcell area: 179342.960330 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1930969
- Blocks: 653047
- Forest area: 173787.21 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 59903
- Scheduled area: 14299.47 ha
- Eligible blocks (age class >= 40): 599030
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 23.15 MB
- Schedules: 0.71 MB
- Runs: 0.00 MB
- Total: 23.85 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
