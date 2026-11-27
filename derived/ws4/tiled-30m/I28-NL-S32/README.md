# WS4 tiled 30-m dataset — I28|NL|S32

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `I28|NL|S32` (parent `I28|NL`)
- Tile / row / col: `I28` / 3 / 2
- Province: `NL`
- Centroid: 53.781961, -66.903940
- Allocated harvest: 5914.830458 m3
- Productive subcell area: 133018.393774 ha
- Committed geometry area: 249916.980479 ha
- Clipped inventory geometry: 249916.980479 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1572513
- Blocks: 594546
- Forest area: 141526.17 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 49487
- Scheduled area: 11671.02 ha
- Eligible blocks (age class >= 40): 494869
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 19.68 MB
- Schedules: 0.58 MB
- Runs: 0.00 MB
- Total: 20.27 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
