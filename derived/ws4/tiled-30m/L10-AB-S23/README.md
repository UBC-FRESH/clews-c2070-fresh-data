# WS4 tiled 30-m dataset — L10|AB|S23

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `L10|AB|S23` (parent `L10|AB`)
- Tile / row / col: `L10` / 2 / 3
- Province: `AB`
- Centroid: 59.902031, -111.516159
- Allocated harvest: 40209.709052 m3
- Productive subcell area: 85859.752264 ha
- Committed geometry area: 106965.235727 ha
- Clipped inventory geometry: 106965.235727 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 979728
- Blocks: 387503
- Forest area: 88175.52 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 36811
- Scheduled area: 7215.21 ha
- Eligible blocks (age class >= 40): 368102
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 12.63 MB
- Schedules: 0.43 MB
- Runs: 0.00 MB
- Total: 13.06 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
