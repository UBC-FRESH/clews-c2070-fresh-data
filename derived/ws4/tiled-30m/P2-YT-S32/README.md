# WS4 tiled 30-m dataset — P2|YT|S32

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `P2|YT|S32` (parent `P2|YT`)
- Tile / row / col: `P2` / 3 / 2
- Province: `YT`
- Centroid: 60.224770, -137.791639
- Allocated harvest: 152.340250 m3
- Productive subcell area: 66232.281697 ha
- Committed geometry area: 233421.408203 ha
- Clipped inventory geometry: 233421.408203 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 437852
- Blocks: 289338
- Forest area: 39406.68 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 25287
- Scheduled area: 3374.91 ha
- Eligible blocks (age class >= 40): 252865
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 7.72 MB
- Schedules: 0.29 MB
- Runs: 0.00 MB
- Total: 8.01 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
