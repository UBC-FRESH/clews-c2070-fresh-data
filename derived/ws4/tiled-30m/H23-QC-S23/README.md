# WS4 tiled 30-m dataset — H23|QC|S23

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `H23|QC|S23` (parent `H23|QC`)
- Tile / row / col: `H23` / 2 / 3
- Province: `QC`
- Centroid: 54.280532, -78.183373
- Allocated harvest: 23899.058181 m3
- Productive subcell area: 129923.086873 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 853516
- Blocks: 284079
- Forest area: 76816.44 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 16916
- Scheduled area: 3632.58 ha
- Eligible blocks (age class >= 40): 169157
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 10.18 MB
- Schedules: 0.20 MB
- Runs: 0.00 MB
- Total: 10.38 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
