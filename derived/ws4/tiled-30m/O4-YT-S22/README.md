# WS4 tiled 30-m dataset — O4|YT|S22

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `O4|YT|S22` (parent `O4|YT`)
- Tile / row / col: `O4` / 2 / 2
- Province: `YT`
- Centroid: 60.314402, -131.092179
- Allocated harvest: 303.480877 m3
- Productive subcell area: 186555.939428 ha
- Committed geometry area: 249970.753620 ha
- Clipped inventory geometry: 249970.753620 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1369936
- Blocks: 805292
- Forest area: 123294.24 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 68942
- Scheduled area: 10327.95 ha
- Eligible blocks (age class >= 40): 689411
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 21.04 MB
- Schedules: 0.82 MB
- Runs: 0.00 MB
- Total: 21.86 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
