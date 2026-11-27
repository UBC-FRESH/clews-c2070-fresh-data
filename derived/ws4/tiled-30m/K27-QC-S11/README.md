# WS4 tiled 30-m dataset — K27|QC|S11

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `K27|QC|S11` (parent `K27|QC`)
- Tile / row / col: `K27` / 1 / 1
- Province: `QC`
- Centroid: 56.209286, -68.474134
- Allocated harvest: 23558.116098 m3
- Productive subcell area: 144369.027546 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1759412
- Blocks: 748674
- Forest area: 158347.08 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 69084
- Scheduled area: 13410.45 ha
- Eligible blocks (age class >= 40): 690834
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 22.35 MB
- Schedules: 0.82 MB
- Runs: 0.00 MB
- Total: 23.17 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
