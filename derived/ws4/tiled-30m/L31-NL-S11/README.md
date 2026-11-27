# WS4 tiled 30-m dataset — L31|NL|S11

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `L31|NL|S11` (parent `L31|NL`)
- Tile / row / col: `L31` / 1 / 1
- Province: `NL`
- Centroid: 54.749464, -58.854558
- Allocated harvest: 5201.739362 m3
- Productive subcell area: 87709.196592 ha
- Committed geometry area: 157814.175444 ha
- Clipped inventory geometry: 157814.175444 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1167313
- Blocks: 395447
- Forest area: 105058.17 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 32105
- Scheduled area: 8573.22 ha
- Eligible blocks (age class >= 40): 321041
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 14.15 MB
- Schedules: 0.38 MB
- Runs: 0.00 MB
- Total: 14.53 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
