# WS4 tiled 30-m dataset — B23|ON|S21

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `B23|ON|S21` (parent `B23|ON`)
- Tile / row / col: `B23` / 2 / 1
- Province: `ON`
- Centroid: 46.569093, -82.469957
- Allocated harvest: 63826.754836 m3
- Productive subcell area: 211174.078444 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2382145
- Blocks: 877691
- Forest area: 214393.05 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 81418
- Scheduled area: 18667.53 ha
- Eligible blocks (age class >= 40): 814172
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 29.80 MB
- Schedules: 0.97 MB
- Runs: 0.00 MB
- Total: 30.77 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
