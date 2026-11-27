# WS4 tiled 30-m dataset — D31|NB|S22

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `D31|NB|S22` (parent `D31|NB`)
- Tile / row / col: `D31` / 2 / 2
- Province: `NB`
- Centroid: 45.531339, -66.086560
- Allocated harvest: 195940.997500 m3
- Productive subcell area: 218446.477389 ha
- Committed geometry area: 249828.578534 ha
- Clipped inventory geometry: 249828.578534 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2188252
- Blocks: 884752
- Forest area: 196942.68 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 75334
- Scheduled area: 15490.26 ha
- Eligible blocks (age class >= 40): 753339
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 27.91 MB
- Schedules: 0.90 MB
- Runs: 0.00 MB
- Total: 28.80 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
