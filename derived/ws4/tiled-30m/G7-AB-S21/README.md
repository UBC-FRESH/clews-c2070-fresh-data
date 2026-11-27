# WS4 tiled 30-m dataset — G7|AB|S21

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `G7|AB|S21` (parent `G7|AB`)
- Tile / row / col: `G7` / 2 / 1
- Province: `AB`
- Centroid: 51.979099, -116.512778
- Allocated harvest: 153012.133424 m3
- Productive subcell area: 173409.438065 ha
- Committed geometry area: 238195.247097 ha
- Clipped inventory geometry: 238195.247097 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1220771
- Blocks: 600600
- Forest area: 109869.39 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 55886
- Scheduled area: 9332.82 ha
- Eligible blocks (age class >= 40): 558858
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 17.47 MB
- Schedules: 0.66 MB
- Runs: 0.00 MB
- Total: 18.13 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
