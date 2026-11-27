# WS4 tiled 30-m dataset — G28|QC|S11

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `G28|QC|S11` (parent `G28|QC`)
- Tile / row / col: `G28` / 1 / 1
- Province: `QC`
- Centroid: 50.642362, -69.980284
- Allocated harvest: 68543.778103 m3
- Productive subcell area: 193904.946491 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2319749
- Blocks: 604729
- Forest area: 208777.41 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 53793
- Scheduled area: 16970.13 ha
- Eligible blocks (age class >= 40): 537921
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 25.47 MB
- Schedules: 0.64 MB
- Runs: 0.00 MB
- Total: 26.10 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
