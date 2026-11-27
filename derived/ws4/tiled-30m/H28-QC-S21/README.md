# WS4 tiled 30-m dataset — H28|QC|S21

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `H28|QC|S21` (parent `H28|QC`)
- Tile / row / col: `H28` / 2 / 1
- Province: `QC`
- Centroid: 52.311292, -68.843127
- Allocated harvest: 37533.593791 m3
- Productive subcell area: 166643.975505 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1993747
- Blocks: 519711
- Forest area: 179437.23 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 45905
- Scheduled area: 16272.99 ha
- Eligible blocks (age class >= 40): 459044
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 21.48 MB
- Schedules: 0.54 MB
- Runs: 0.00 MB
- Total: 22.02 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
