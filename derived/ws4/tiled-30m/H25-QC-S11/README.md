# WS4 tiled 30-m dataset — H25|QC|S11

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `H25|QC|S11` (parent `H25|QC`)
- Tile / row / col: `H25` / 1 / 1
- Province: `QC`
- Centroid: 53.327387, -75.441391
- Allocated harvest: 25508.357719 m3
- Productive subcell area: 130246.271619 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1461860
- Blocks: 218319
- Forest area: 131567.40 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 9819
- Scheduled area: 1491.57 ha
- Eligible blocks (age class >= 40): 98181
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 11.90 MB
- Schedules: 0.11 MB
- Runs: 0.00 MB
- Total: 12.01 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
