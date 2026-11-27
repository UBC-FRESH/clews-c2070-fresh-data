# WS4 tiled 30-m dataset — M6|BC|S33

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `M6|BC|S33` (parent `M6|BC`)
- Tile / row / col: `M6` / 3 / 3
- Province: `BC`
- Centroid: 59.818905, -123.195813
- Allocated harvest: 87800.573134 m3
- Productive subcell area: 180247.179011 ha
- Committed geometry area: 208786.000487 ha
- Clipped inventory geometry: 208786.000487 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2045083
- Blocks: 767754
- Forest area: 184057.47 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 71654
- Scheduled area: 16739.19 ha
- Eligible blocks (age class >= 40): 716537
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 25.31 MB
- Schedules: 0.85 MB
- Runs: 0.00 MB
- Total: 26.16 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
