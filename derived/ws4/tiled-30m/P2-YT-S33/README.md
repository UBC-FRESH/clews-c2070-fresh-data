# WS4 tiled 30-m dataset — P2|YT|S33

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `P2|YT|S33` (parent `P2|YT`)
- Tile / row / col: `P2` / 3 / 3
- Province: `YT`
- Centroid: 60.493032, -137.062015
- Allocated harvest: 163.160110 m3
- Productive subcell area: 70936.383050 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1255079
- Blocks: 800217
- Forest area: 112957.11 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 74012
- Scheduled area: 10102.86 ha
- Eligible blocks (age class >= 40): 740112
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 20.40 MB
- Schedules: 0.88 MB
- Runs: 0.00 MB
- Total: 21.28 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
