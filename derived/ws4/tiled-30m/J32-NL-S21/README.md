# WS4 tiled 30-m dataset — J32|NL|S21

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `J32|NL|S21` (parent `J32|NL`)
- Tile / row / col: `J32` / 2 / 1
- Province: `NL`
- Centroid: 52.185918, -58.910835
- Allocated harvest: 9913.992542 m3
- Productive subcell area: 169306.119030 ha
- Committed geometry area: 216970.515613 ha
- Clipped inventory geometry: 216970.515613 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1994936
- Blocks: 755200
- Forest area: 179544.24 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 69561
- Scheduled area: 16794.36 ha
- Eligible blocks (age class >= 40): 695606
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 24.91 MB
- Schedules: 0.82 MB
- Runs: 0.00 MB
- Total: 25.73 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
