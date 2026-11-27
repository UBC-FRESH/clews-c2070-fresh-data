# WS4 tiled 30-m dataset — D32|NS|S12

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `D32|NS|S12` (parent `D32|NS`)
- Tile / row / col: `D32` / 1 / 2
- Province: `NS`
- Centroid: 44.540302, -64.694334
- Allocated harvest: 117727.321813 m3
- Productive subcell area: 203583.827434 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2364966
- Blocks: 1039200
- Forest area: 212846.94 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 90847
- Scheduled area: 16454.97 ha
- Eligible blocks (age class >= 40): 908469
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 31.88 MB
- Schedules: 1.08 MB
- Runs: 0.00 MB
- Total: 32.96 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
