# WS4 tiled 30-m dataset — E5|BC|S33

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `E5|BC|S33` (parent `E5|BC`)
- Tile / row / col: `E5` / 3 / 3
- Province: `BC`
- Centroid: 49.232774, -117.969748
- Allocated harvest: 169488.621955 m3
- Productive subcell area: 202851.317153 ha
- Committed geometry area: 241864.550476 ha
- Clipped inventory geometry: 241864.550476 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2355925
- Blocks: 1066264
- Forest area: 212033.25 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 96428
- Scheduled area: 16455.06 ha
- Eligible blocks (age class >= 40): 964279
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 32.05 MB
- Schedules: 1.15 MB
- Runs: 0.00 MB
- Total: 33.20 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
