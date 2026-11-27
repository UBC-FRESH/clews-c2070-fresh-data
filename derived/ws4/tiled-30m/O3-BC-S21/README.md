# WS4 tiled 30-m dataset — O3|BC|S21

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `O3|BC|S21` (parent `O3|BC`)
- Tile / row / col: `O3` / 2 / 1
- Province: `BC`
- Centroid: 59.284737, -134.134599
- Allocated harvest: 56414.204122 m3
- Productive subcell area: 138591.993275 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 800773
- Blocks: 479192
- Forest area: 72069.57 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 43502
- Scheduled area: 6173.64 ha
- Eligible blocks (age class >= 40): 435017
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 12.64 MB
- Schedules: 0.51 MB
- Runs: 0.00 MB
- Total: 13.15 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
