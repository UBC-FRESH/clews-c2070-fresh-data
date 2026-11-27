# WS4 tiled 30-m dataset — I13|SK|S23

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `I13|SK|S23` (parent `I13|SK`)
- Tile / row / col: `I13` / 2 / 3
- Province: `SK`
- Centroid: 56.723841, -102.362830
- Allocated harvest: 23424.616678 m3
- Productive subcell area: 146260.534870 ha
- Committed geometry area: 213573.201352 ha
- Clipped inventory geometry: 213573.201352 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 615738
- Blocks: 155328
- Forest area: 55416.42 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 13418
- Scheduled area: 4497.03 ha
- Eligible blocks (age class >= 40): 134176
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 6.98 MB
- Schedules: 0.15 MB
- Runs: 0.00 MB
- Total: 7.13 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
