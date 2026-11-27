# WS4 tiled 30-m dataset — E13|SK|S12

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `E13|SK|S12` (parent `E13|SK`)
- Tile / row / col: `E13` / 1 / 2
- Province: `SK`
- Centroid: 50.777791, -101.948126
- Allocated harvest: 7564.483900 m3
- Productive subcell area: 34376.961027 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 195882
- Blocks: 74000
- Forest area: 17629.38 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 4081
- Scheduled area: 1399.68 ha
- Eligible blocks (age class >= 40): 40809
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 2.92 MB
- Schedules: 0.04 MB
- Runs: 0.00 MB
- Total: 2.96 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
