# WS4 tiled 30-m dataset — H25|QC|S21

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `H25|QC|S21` (parent `H25|QC`)
- Tile / row / col: `H25` / 2 / 1
- Province: `QC`
- Centroid: 53.761890, -75.208249
- Allocated harvest: 25508.357719 m3
- Productive subcell area: 130246.271619 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1053062
- Blocks: 373499
- Forest area: 94775.58 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 31819
- Scheduled area: 6647.49 ha
- Eligible blocks (age class >= 40): 318187
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 12.59 MB
- Schedules: 0.37 MB
- Runs: 0.00 MB
- Total: 12.96 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
