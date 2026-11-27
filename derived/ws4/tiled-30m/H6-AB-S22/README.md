# WS4 tiled 30-m dataset — H6|AB|S22

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `H6|AB|S22` (parent `H6|AB`)
- Tile / row / col: `H6` / 2 / 2
- Province: `AB`
- Centroid: 53.006195, -118.492044
- Allocated harvest: 41378.269835 m3
- Productive subcell area: 51589.183590 ha
- Committed geometry area: 89464.622965 ha
- Clipped inventory geometry: 89464.622965 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 508932
- Blocks: 251566
- Forest area: 45803.88 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 23548
- Scheduled area: 4337.82 ha
- Eligible blocks (age class >= 40): 235475
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 7.80 MB
- Schedules: 0.27 MB
- Runs: 0.00 MB
- Total: 8.08 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
