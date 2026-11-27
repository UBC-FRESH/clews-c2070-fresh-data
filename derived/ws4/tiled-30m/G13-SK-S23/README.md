# WS4 tiled 30-m dataset — G13|SK|S23

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `G13|SK|S23` (parent `G13|SK`)
- Tile / row / col: `G13` / 2 / 3
- Province: `SK`
- Centroid: 53.980892, -101.969609
- Allocated harvest: 19220.359332 m3
- Productive subcell area: 85562.475807 ha
- Committed geometry area: 120113.822280 ha
- Clipped inventory geometry: 120113.822280 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 941327
- Blocks: 352144
- Forest area: 84719.43 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 33511
- Scheduled area: 7641.99 ha
- Eligible blocks (age class >= 40): 335104
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 11.96 MB
- Schedules: 0.39 MB
- Runs: 0.00 MB
- Total: 12.35 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
