# WS4 tiled 30-m dataset — E7|BC|S21

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `E7|BC|S21` (parent `E7|BC`)
- Tile / row / col: `E7` / 2 / 1
- Province: `BC`
- Centroid: 49.398729, -115.147683
- Allocated harvest: 158951.994403 m3
- Productive subcell area: 187227.665486 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2139654
- Blocks: 1106842
- Forest area: 192568.86 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 97956
- Scheduled area: 14797.62 ha
- Eligible blocks (age class >= 40): 979560
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 30.70 MB
- Schedules: 1.17 MB
- Runs: 0.00 MB
- Total: 31.88 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
