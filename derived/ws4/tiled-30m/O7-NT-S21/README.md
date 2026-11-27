# WS4 tiled 30-m dataset — O7|NT|S21

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `O7|NT|S21` (parent `O7|NT`)
- Tile / row / col: `O7` / 2 / 1
- Province: `NT`
- Centroid: 62.137849, -124.413891
- Allocated harvest: 178.486937 m3
- Productive subcell area: 176484.661366 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1968369
- Blocks: 844974
- Forest area: 177153.21 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 72585
- Scheduled area: 13797.00 ha
- Eligible blocks (age class >= 40): 725842
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 25.88 MB
- Schedules: 0.86 MB
- Runs: 0.00 MB
- Total: 26.74 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
