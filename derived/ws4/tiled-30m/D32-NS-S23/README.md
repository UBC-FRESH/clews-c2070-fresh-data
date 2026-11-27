# WS4 tiled 30-m dataset — D32|NS|S23

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `D32|NS|S23` (parent `D32|NS`)
- Tile / row / col: `D32` / 2 / 3
- Province: `NS`
- Centroid: 44.740154, -63.856387
- Allocated harvest: 107834.315669 m3
- Productive subcell area: 186476.022511 ha
- Committed geometry area: 228991.694553 ha
- Clipped inventory geometry: 228991.694553 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1983300
- Blocks: 695402
- Forest area: 178497.00 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 59611
- Scheduled area: 13638.69 ha
- Eligible blocks (age class >= 40): 596103
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 24.04 MB
- Schedules: 0.71 MB
- Runs: 0.00 MB
- Total: 24.75 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
