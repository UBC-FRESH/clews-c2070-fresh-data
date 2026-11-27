# WS4 tiled 30-m dataset — N5|NT|S33

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `N5|NT|S33` (parent `N5|NT`)
- Tile / row / col: `N5` / 3 / 3
- Province: `NT`
- Centroid: 60.761619, -126.769081
- Allocated harvest: 0.360289 m3
- Productive subcell area: 309.727633 ha
- Committed geometry area: 361.268187 ha
- Clipped inventory geometry: 361.268187 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 3810
- Blocks: 1565
- Forest area: 342.90 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 1477
- Scheduled area: 331.38 ha
- Eligible blocks (age class >= 40): 1477
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 0.13 MB
- Schedules: 0.01 MB
- Runs: 0.00 MB
- Total: 0.14 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
