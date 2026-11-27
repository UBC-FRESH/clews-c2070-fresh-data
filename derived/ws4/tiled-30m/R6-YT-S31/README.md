# WS4 tiled 30-m dataset — R6|YT|S31

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `R6|YT|S31` (parent `R6|YT`)
- Tile / row / col: `R6` / 3 / 1
- Province: `YT`
- Centroid: 65.500369, -132.621612
- Allocated harvest: 62.609476 m3
- Productive subcell area: 53959.852886 ha
- Committed geometry area: 119649.481449 ha
- Clipped inventory geometry: 119649.481449 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 470024
- Blocks: 182839
- Forest area: 42302.16 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 12058
- Scheduled area: 2173.23 ha
- Eligible blocks (age class >= 40): 120578
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 6.55 MB
- Schedules: 0.14 MB
- Runs: 0.00 MB
- Total: 6.69 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
