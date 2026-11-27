# WS4 tiled 30-m dataset — I10|SK|S12

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `I10|SK|S12` (parent `I10|SK`)
- Tile / row / col: `I10` / 1 / 2
- Province: `SK`
- Centroid: 55.454856, -109.915363
- Allocated harvest: 7815.698647 m3
- Productive subcell area: 40387.104654 ha
- Committed geometry area: 47868.803059 ha
- Clipped inventory geometry: 47868.803059 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 457505
- Blocks: 141547
- Forest area: 41175.45 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 10117
- Scheduled area: 2365.29 ha
- Eligible blocks (age class >= 40): 101167
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 5.80 MB
- Schedules: 0.11 MB
- Runs: 0.00 MB
- Total: 5.91 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
