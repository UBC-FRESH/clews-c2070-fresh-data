# WS4 tiled 30-m dataset — K7|AB|S22

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `K7|AB|S22` (parent `K7|AB`)
- Tile / row / col: `K7` / 2 / 2
- Province: `AB`
- Centroid: 57.267639, -119.103223
- Allocated harvest: 136701.137684 m3
- Productive subcell area: 235257.878114 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2717868
- Blocks: 871400
- Forest area: 244608.12 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 83093
- Scheduled area: 20312.28 ha
- Eligible blocks (age class >= 40): 830925
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 30.53 MB
- Schedules: 0.99 MB
- Runs: 0.00 MB
- Total: 31.52 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
