# WS4 tiled 30-m dataset — J2|BC|S32

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `J2|BC|S32` (parent `J2|BC`)
- Tile / row / col: `J2` / 3 / 2
- Province: `BC`
- Centroid: 53.547965, -129.068479
- Allocated harvest: 94258.041283 m3
- Productive subcell area: 124250.714224 ha
- Committed geometry area: 170171.733882 ha
- Clipped inventory geometry: 170171.733882 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1627023
- Blocks: 835322
- Forest area: 146432.07 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 81760
- Scheduled area: 13918.86 ha
- Eligible blocks (age class >= 40): 817593
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 22.95 MB
- Schedules: 0.97 MB
- Runs: 0.00 MB
- Total: 23.92 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
