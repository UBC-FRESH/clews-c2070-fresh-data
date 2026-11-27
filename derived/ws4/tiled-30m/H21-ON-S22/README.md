# WS4 tiled 30-m dataset — H21|ON|S22

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `H21|ON|S22` (parent `H21|ON`)
- Tile / row / col: `H21` / 2 / 2
- Province: `ON`
- Centroid: 54.986276, -83.568839
- Allocated harvest: 4130.182680 m3
- Productive subcell area: 76262.873888 ha
- Committed geometry area: 249957.782878 ha
- Clipped inventory geometry: 249957.782878 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 482193
- Blocks: 209286
- Forest area: 43397.37 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 16469
- Scheduled area: 3647.52 ha
- Eligible blocks (age class >= 40): 164688
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 6.99 MB
- Schedules: 0.19 MB
- Runs: 0.00 MB
- Total: 7.18 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
