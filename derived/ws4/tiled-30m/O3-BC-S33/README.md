# WS4 tiled 30-m dataset — O3|BC|S33

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `O3|BC|S33` (parent `O3|BC`)
- Tile / row / col: `O3` / 3 / 3
- Province: `BC`
- Centroid: 59.957015, -133.207078
- Allocated harvest: 4857.450737 m3
- Productive subcell area: 11933.231894 ha
- Committed geometry area: 21525.832070 ha
- Clipped inventory geometry: 21525.832070 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 219017
- Blocks: 105239
- Forest area: 19711.53 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 10121
- Scheduled area: 1892.88 ha
- Eligible blocks (age class >= 40): 101209
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 3.78 MB
- Schedules: 0.11 MB
- Runs: 0.00 MB
- Total: 3.89 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
