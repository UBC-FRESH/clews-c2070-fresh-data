# WS4 tiled 30-m dataset — H30|NL|S31

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `H30|NL|S31` (parent `H30|NL`)
- Tile / row / col: `H30` / 3 / 1
- Province: `NL`
- Centroid: 51.722898, -64.548208
- Allocated harvest: 2387.796329 m3
- Productive subcell area: 32669.316338 ha
- Committed geometry area: 45468.999325 ha
- Clipped inventory geometry: 45468.999325 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 395683
- Blocks: 173241
- Forest area: 35611.47 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 15815
- Scheduled area: 3699.36 ha
- Eligible blocks (age class >= 40): 158148
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 5.94 MB
- Schedules: 0.18 MB
- Runs: 0.00 MB
- Total: 6.12 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
