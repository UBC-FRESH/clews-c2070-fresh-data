# WS4 tiled 30-m dataset — D21|ON|S33

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `D21|ON|S33` (parent `D21|ON`)
- Tile / row / col: `D21` / 3 / 3
- Province: `ON`
- Centroid: 49.981541, -84.256243
- Allocated harvest: 43833.125097 m3
- Productive subcell area: 223173.850989 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2657862
- Blocks: 939280
- Forest area: 239207.58 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 89446
- Scheduled area: 21471.12 ha
- Eligible blocks (age class >= 40): 894456
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 32.10 MB
- Schedules: 1.06 MB
- Runs: 0.00 MB
- Total: 33.16 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
