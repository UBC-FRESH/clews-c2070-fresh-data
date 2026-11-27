# WS4 tiled 30-m dataset — K7|AB|S23

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `K7|AB|S23` (parent `K7|AB`)
- Tile / row / col: `K7` / 2 / 3
- Province: `AB`
- Centroid: 57.435147, -118.310659
- Allocated harvest: 136701.137684 m3
- Productive subcell area: 235257.878114 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2747000
- Blocks: 1102566
- Forest area: 247230.00 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 105042
- Scheduled area: 21928.50 ha
- Eligible blocks (age class >= 40): 1050416
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 34.90 MB
- Schedules: 1.26 MB
- Runs: 0.00 MB
- Total: 36.16 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
