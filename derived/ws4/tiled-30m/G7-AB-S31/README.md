# WS4 tiled 30-m dataset — G7|AB|S31

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `G7|AB|S31` (parent `G7|AB`)
- Tile / row / col: `G7` / 3 / 1
- Province: `AB`
- Centroid: 52.396372, -116.768541
- Allocated harvest: 160595.284005 m3
- Productive subcell area: 182003.461634 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1188851
- Blocks: 534438
- Forest area: 106996.59 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 50169
- Scheduled area: 9761.58 ha
- Eligible blocks (age class >= 40): 501685
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 16.47 MB
- Schedules: 0.59 MB
- Runs: 0.00 MB
- Total: 17.06 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
