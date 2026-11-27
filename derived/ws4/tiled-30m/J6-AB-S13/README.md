# WS4 tiled 30-m dataset — J6|AB|S13

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `J6|AB|S13` (parent `J6|AB`)
- Tile / row / col: `J6` / 1 / 3
- Province: `AB`
- Centroid: 55.221780, -119.406378
- Allocated harvest: 105402.863903 m3
- Productive subcell area: 147273.917545 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 871096
- Blocks: 382703
- Forest area: 78398.64 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 30257
- Scheduled area: 6407.37 ha
- Eligible blocks (age class >= 40): 302566
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 11.87 MB
- Schedules: 0.35 MB
- Runs: 0.00 MB
- Total: 12.22 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
