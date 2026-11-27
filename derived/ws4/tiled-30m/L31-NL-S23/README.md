# WS4 tiled 30-m dataset — L31|NL|S23

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `L31|NL|S23` (parent `L31|NL`)
- Tile / row / col: `L31` / 2 / 3
- Province: `NL`
- Centroid: 54.637402, -57.496309
- Allocated harvest: 419.992508 m3
- Productive subcell area: 7081.709194 ha
- Committed geometry area: 12742.040067 ha
- Clipped inventory geometry: 12742.040067 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 36569
- Blocks: 13774
- Forest area: 3291.21 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 583
- Scheduled area: 81.00 ha
- Eligible blocks (age class >= 40): 5821
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 0.61 MB
- Schedules: 0.01 MB
- Runs: 0.00 MB
- Total: 0.62 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
