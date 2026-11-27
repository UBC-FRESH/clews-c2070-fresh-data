# WS4 tiled 30-m dataset — Q6|YT|S11

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `Q6|YT|S11` (parent `Q6|YT`)
- Tile / row / col: `Q6` / 1 / 1
- Province: `YT`
- Centroid: 63.505796, -129.997095
- Allocated harvest: 7.444789 m3
- Productive subcell area: 6663.298768 ha
- Committed geometry area: 26395.114650 ha
- Clipped inventory geometry: 26395.114650 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 22477
- Blocks: 14075
- Forest area: 2022.93 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 1510
- Scheduled area: 183.42 ha
- Eligible blocks (age class >= 40): 1510
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 0.49 MB
- Schedules: 0.02 MB
- Runs: 0.00 MB
- Total: 0.51 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
