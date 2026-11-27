# WS4 tiled 30-m dataset — I35|NL|S33

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `I35|NL|S33` (parent `I35|NL`)
- Tile / row / col: `I35` / 3 / 3
- Province: `NL`
- Centroid: 48.488543, -53.334048
- Allocated harvest: 5289.037897 m3
- Productive subcell area: 69334.254664 ha
- Committed geometry area: 106496.916670 ha
- Clipped inventory geometry: 106496.916670 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 916585
- Blocks: 425292
- Forest area: 82492.65 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 39028
- Scheduled area: 7619.13 ha
- Eligible blocks (age class >= 40): 390275
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 12.76 MB
- Schedules: 0.46 MB
- Runs: 0.00 MB
- Total: 13.22 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
