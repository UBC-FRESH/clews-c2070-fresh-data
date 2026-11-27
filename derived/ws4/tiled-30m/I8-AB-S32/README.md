# WS4 tiled 30-m dataset — I8|AB|S32

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `I8|AB|S32` (parent `I8|AB`)
- Tile / row / col: `I8` / 3 / 2
- Province: `AB`
- Centroid: 55.581326, -115.348639
- Allocated harvest: 138788.880765 m3
- Productive subcell area: 208941.887280 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1758939
- Blocks: 584142
- Forest area: 158304.51 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 53255
- Scheduled area: 12857.04 ha
- Eligible blocks (age class >= 40): 532542
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 21.16 MB
- Schedules: 0.63 MB
- Runs: 0.00 MB
- Total: 21.79 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
