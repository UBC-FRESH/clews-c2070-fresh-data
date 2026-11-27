# WS4 tiled 30-m dataset — H21|ON|S23

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `H21|ON|S23` (parent `H21|ON`)
- Tile / row / col: `H21` / 2 / 3
- Province: `ON`
- Centroid: 54.900708, -82.789091
- Allocated harvest: 4108.819329 m3
- Productive subcell area: 75868.404517 ha
- Committed geometry area: 248664.877375 ha
- Clipped inventory geometry: 248664.877375 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 197338
- Blocks: 76521
- Forest area: 17760.42 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 5272
- Scheduled area: 1320.12 ha
- Eligible blocks (age class >= 40): 52711
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 3.05 MB
- Schedules: 0.06 MB
- Runs: 0.00 MB
- Total: 3.11 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
