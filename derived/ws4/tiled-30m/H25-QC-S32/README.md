# WS4 tiled 30-m dataset — H25|QC|S32

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `H25|QC|S32` (parent `H25|QC`)
- Tile / row / col: `H25` / 3 / 2
- Province: `QC`
- Centroid: 54.052349, -74.231572
- Allocated harvest: 25508.357719 m3
- Productive subcell area: 130246.271619 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1473948
- Blocks: 379202
- Forest area: 132655.32 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 27590
- Scheduled area: 5958.09 ha
- Eligible blocks (age class >= 40): 275899
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 15.14 MB
- Schedules: 0.33 MB
- Runs: 0.00 MB
- Total: 15.46 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
