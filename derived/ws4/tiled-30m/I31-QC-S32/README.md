# WS4 tiled 30-m dataset — I31|QC|S32

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `I31|QC|S32` (parent `I31|QC`)
- Tile / row / col: `I31` / 3 / 2
- Province: `QC`
- Centroid: 51.818588, -60.925152
- Allocated harvest: 48866.513431 m3
- Productive subcell area: 166683.531729 ha
- Committed geometry area: 209776.140185 ha
- Clipped inventory geometry: 209776.140185 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1956718
- Blocks: 550286
- Forest area: 176104.62 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 52453
- Scheduled area: 19564.47 ha
- Eligible blocks (age class >= 40): 524527
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 21.76 MB
- Schedules: 0.62 MB
- Runs: 0.00 MB
- Total: 22.38 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
