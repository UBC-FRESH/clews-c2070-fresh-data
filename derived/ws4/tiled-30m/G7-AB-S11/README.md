# WS4 tiled 30-m dataset — G7|AB|S11

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `G7|AB|S11` (parent `G7|AB`)
- Tile / row / col: `G7` / 1 / 1
- Province: `AB`
- Centroid: 51.572923, -116.178707
- Allocated harvest: 109420.962049 m3
- Productive subcell area: 124007.339266 ha
- Committed geometry area: 170336.511945 ha
- Clipped inventory geometry: 170336.511945 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 732680
- Blocks: 402551
- Forest area: 65941.20 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 37994
- Scheduled area: 6122.16 ha
- Eligible blocks (age class >= 40): 379935
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 11.24 MB
- Schedules: 0.45 MB
- Runs: 0.00 MB
- Total: 11.69 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
