# WS4 tiled 30-m dataset — A24|ON|S11

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `A24|ON|S11` (parent `A24|ON`)
- Tile / row / col: `A24` / 1 / 1
- Province: `ON`
- Centroid: 44.538541, -81.100504
- Allocated harvest: 24474.235249 m3
- Productive subcell area: 94024.180735 ha
- Committed geometry area: 195965.719746 ha
- Clipped inventory geometry: 195965.719746 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 983551
- Blocks: 340191
- Forest area: 88519.59 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 25372
- Scheduled area: 7093.35 ha
- Eligible blocks (age class >= 40): 253711
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 12.00 MB
- Schedules: 0.30 MB
- Runs: 0.00 MB
- Total: 12.29 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
