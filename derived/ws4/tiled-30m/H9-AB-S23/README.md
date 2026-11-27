# WS4 tiled 30-m dataset — H9|AB|S23

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `H9|AB|S23` (parent `H9|AB`)
- Tile / row / col: `H9` / 2 / 3
- Province: `AB`
- Centroid: 54.347012, -111.390995
- Allocated harvest: 70941.191131 m3
- Productive subcell area: 142483.335016 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1374873
- Blocks: 533706
- Forest area: 123738.57 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 44141
- Scheduled area: 10148.85 ha
- Eligible blocks (age class >= 40): 441406
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 17.77 MB
- Schedules: 0.52 MB
- Runs: 0.00 MB
- Total: 18.29 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
