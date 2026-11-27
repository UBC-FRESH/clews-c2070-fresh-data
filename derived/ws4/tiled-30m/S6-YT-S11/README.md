# WS4 tiled 30-m dataset — S6|YT|S11

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `S6|YT|S11` (parent `S6|YT`)
- Tile / row / col: `S6` / 1 / 1
- Province: `YT`
- Centroid: 65.794174, -133.051051
- Allocated harvest: 243.858920 m3
- Productive subcell area: 133867.635112 ha
- Committed geometry area: 193304.031732 ha
- Clipped inventory geometry: 193304.031732 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1872239
- Blocks: 669585
- Forest area: 168501.51 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 55910
- Scheduled area: 13140.54 ha
- Eligible blocks (age class >= 40): 559099
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 22.68 MB
- Schedules: 0.66 MB
- Runs: 0.00 MB
- Total: 23.34 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
