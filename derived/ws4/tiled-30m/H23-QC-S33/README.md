# WS4 tiled 30-m dataset — H23|QC|S33

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `H23|QC|S33` (parent `H23|QC`)
- Tile / row / col: `H23` / 3 / 3
- Province: `QC`
- Centroid: 54.721713, -77.976833
- Allocated harvest: 23899.058181 m3
- Productive subcell area: 129923.086873 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1363147
- Blocks: 539972
- Forest area: 122683.23 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 42626
- Scheduled area: 9796.86 ha
- Eligible blocks (age class >= 40): 426254
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 17.38 MB
- Schedules: 0.50 MB
- Runs: 0.00 MB
- Total: 17.88 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
