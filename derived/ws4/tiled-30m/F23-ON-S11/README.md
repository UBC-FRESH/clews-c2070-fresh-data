# WS4 tiled 30-m dataset — F23|ON|S11

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `F23|ON|S11` (parent `F23|ON`)
- Tile / row / col: `F23` / 1 / 1
- Province: `ON`
- Centroid: 51.405090, -80.911264
- Allocated harvest: 11233.053427 m3
- Productive subcell area: 170730.354603 ha
- Committed geometry area: 248812.704217 ha
- Clipped inventory geometry: 248812.704217 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1791843
- Blocks: 706051
- Forest area: 161265.87 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 67554
- Scheduled area: 14122.53 ha
- Eligible blocks (age class >= 40): 675534
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 22.59 MB
- Schedules: 0.80 MB
- Runs: 0.00 MB
- Total: 23.39 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
