# WS4 tiled 30-m dataset — O10|NT|S11

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `O10|NT|S11` (parent `O10|NT`)
- Tile / row / col: `O10` / 1 / 1
- Province: `NT`
- Centroid: 63.309592, -115.642285
- Allocated harvest: 51.633304 m3
- Productive subcell area: 87530.451398 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1254894
- Blocks: 632779
- Forest area: 112940.46 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 38461
- Scheduled area: 6528.87 ha
- Eligible blocks (age class >= 40): 384607
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 17.68 MB
- Schedules: 0.45 MB
- Runs: 0.00 MB
- Total: 18.13 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
