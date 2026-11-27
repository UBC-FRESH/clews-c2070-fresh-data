# WS4 tiled 30-m dataset — O6|NT|S33

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `O6|NT|S33` (parent `O6|NT`)
- Tile / row / col: `O6` / 3 / 3
- Province: `NT`
- Centroid: 62.338925, -125.748150
- Allocated harvest: 101.797925 m3
- Productive subcell area: 122838.100117 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 575803
- Blocks: 306603
- Forest area: 51822.27 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 24079
- Scheduled area: 4026.24 ha
- Eligible blocks (age class >= 40): 240782
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 8.86 MB
- Schedules: 0.28 MB
- Runs: 0.00 MB
- Total: 9.14 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
