# WS4 tiled 30-m dataset — L9|AB|S32

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `L9|AB|S32` (parent `L9|AB`)
- Tile / row / col: `L9` / 3 / 2
- Province: `AB`
- Centroid: 59.861184, -115.318935
- Allocated harvest: 60911.942144 m3
- Productive subcell area: 121952.543238 ha
- Committed geometry area: 155347.519359 ha
- Clipped inventory geometry: 155347.519359 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1503788
- Blocks: 435609
- Forest area: 135340.92 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 37399
- Scheduled area: 7804.26 ha
- Eligible blocks (age class >= 40): 373985
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 16.54 MB
- Schedules: 0.44 MB
- Runs: 0.00 MB
- Total: 16.98 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
