# WS4 tiled 30-m dataset — R9|NT|S21

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `R9|NT|S21` (parent `R9|NT`)
- Tile / row / col: `R9` / 2 / 1
- Province: `NT`
- Centroid: 67.092858, -122.807928
- Allocated harvest: 2.492509 m3
- Productive subcell area: 6703.253447 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 787666
- Blocks: 410182
- Forest area: 70889.94 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 30389
- Scheduled area: 5212.08 ha
- Eligible blocks (age class >= 40): 303883
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 11.51 MB
- Schedules: 0.36 MB
- Runs: 0.00 MB
- Total: 11.86 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
