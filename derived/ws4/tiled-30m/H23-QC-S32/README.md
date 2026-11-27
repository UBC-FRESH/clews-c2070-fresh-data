# WS4 tiled 30-m dataset — H23|QC|S32

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `H23|QC|S32` (parent `H23|QC`)
- Tile / row / col: `H23` / 3 / 2
- Province: `QC`
- Centroid: 54.780548, -78.688631
- Allocated harvest: 16739.674202 m3
- Productive subcell area: 91002.336957 ha
- Committed geometry area: 175108.095003 ha
- Clipped inventory geometry: 175108.095003 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 908379
- Blocks: 411072
- Forest area: 81754.11 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 34386
- Scheduled area: 6683.31 ha
- Eligible blocks (age class >= 40): 343855
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 12.25 MB
- Schedules: 0.40 MB
- Runs: 0.00 MB
- Total: 12.66 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
