# WS4 tiled 30-m dataset — H3|BC|S13

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `H3|BC|S13` (parent `H3|BC`)
- Tile / row / col: `H3` / 1 / 3
- Province: `BC`
- Centroid: 51.056320, -123.792226
- Allocated harvest: 91768.239037 m3
- Productive subcell area: 139257.618241 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 800403
- Blocks: 481080
- Forest area: 72036.27 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 44001
- Scheduled area: 6282.81 ha
- Eligible blocks (age class >= 40): 440010
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 12.73 MB
- Schedules: 0.52 MB
- Runs: 0.00 MB
- Total: 13.24 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
