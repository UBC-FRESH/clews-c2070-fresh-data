# WS4 tiled 30-m dataset — I30|QC|S12

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `I30|QC|S12` (parent `I30|QC`)
- Tile / row / col: `I30` / 1 / 2
- Province: `QC`
- Centroid: 51.733379, -63.561540
- Allocated harvest: 42654.950860 m3
- Productive subcell area: 188944.940368 ha
- Committed geometry area: 246827.190471 ha
- Clipped inventory geometry: 246827.190471 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2182200
- Blocks: 767693
- Forest area: 196398.00 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 71925
- Scheduled area: 17715.24 ha
- Eligible blocks (age class >= 40): 719247
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 26.15 MB
- Schedules: 0.85 MB
- Runs: 0.00 MB
- Total: 27.01 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
