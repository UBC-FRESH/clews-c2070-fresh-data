# WS4 tiled 30-m dataset — H35|NL|S23

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `H35|NL|S23` (parent `H35|NL`)
- Tile / row / col: `H35` / 2 / 3
- Province: `NL`
- Centroid: 47.205616, -55.134695
- Allocated harvest: 2675.383411 m3
- Productive subcell area: 36090.821376 ha
- Committed geometry area: 75352.413217 ha
- Clipped inventory geometry: 75352.413217 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 561214
- Blocks: 264810
- Forest area: 50509.26 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 23180
- Scheduled area: 4526.82 ha
- Eligible blocks (age class >= 40): 231791
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 8.24 MB
- Schedules: 0.27 MB
- Runs: 0.00 MB
- Total: 8.51 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
