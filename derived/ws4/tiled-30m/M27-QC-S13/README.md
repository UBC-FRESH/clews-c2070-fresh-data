# WS4 tiled 30-m dataset — M27|QC|S13

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `M27|QC|S13` (parent `M27|QC`)
- Tile / row / col: `M27` / 1 / 3
- Province: `QC`
- Centroid: 58.303026, -64.747128
- Allocated harvest: 3549.818080 m3
- Productive subcell area: 19378.438459 ha
- Committed geometry area: 248317.668021 ha
- Clipped inventory geometry: 248317.668021 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 35615
- Blocks: 19782
- Forest area: 3205.35 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 1095
- Scheduled area: 184.23 ha
- Eligible blocks (age class >= 40): 10941
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 0.73 MB
- Schedules: 0.01 MB
- Runs: 0.00 MB
- Total: 0.74 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
