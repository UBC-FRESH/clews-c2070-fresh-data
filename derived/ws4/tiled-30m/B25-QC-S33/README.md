# WS4 tiled 30-m dataset — B25|QC|S33

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `B25|QC|S33` (parent `B25|QC`)
- Tile / row / col: `B25` / 3 / 3
- Province: `QC`
- Centroid: 46.195966, -77.271898
- Allocated harvest: 94255.172904 m3
- Productive subcell area: 168265.798409 ha
- Committed geometry area: 197847.949779 ha
- Clipped inventory geometry: 197847.949779 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1917772
- Blocks: 628045
- Forest area: 172599.48 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 59950
- Scheduled area: 16271.64 ha
- Eligible blocks (age class >= 40): 599499
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 22.96 MB
- Schedules: 0.71 MB
- Runs: 0.00 MB
- Total: 23.67 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
