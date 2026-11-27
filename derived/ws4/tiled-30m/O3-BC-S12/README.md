# WS4 tiled 30-m dataset — O3|BC|S12

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `O3|BC|S12` (parent `O3|BC`)
- Tile / row / col: `O3` / 1 / 2
- Province: `BC`
- Centroid: 59.167953, -132.882355
- Allocated harvest: 56414.204122 m3
- Productive subcell area: 138591.993275 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1826355
- Blocks: 1006834
- Forest area: 164371.95 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 94131
- Scheduled area: 14824.53 ha
- Eligible blocks (age class >= 40): 941305
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 26.76 MB
- Schedules: 1.12 MB
- Runs: 0.00 MB
- Total: 27.88 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
