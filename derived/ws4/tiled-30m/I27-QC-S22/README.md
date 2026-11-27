# WS4 tiled 30-m dataset — I27|QC|S22

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `I27|QC|S22` (parent `I27|QC`)
- Tile / row / col: `I27` / 2 / 2
- Province: `QC`
- Centroid: 53.927326, -69.333671
- Allocated harvest: 17088.057852 m3
- Productive subcell area: 130072.193185 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1207602
- Blocks: 373336
- Forest area: 108684.18 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 32307
- Scheduled area: 9599.31 ha
- Eligible blocks (age class >= 40): 323063
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 13.91 MB
- Schedules: 0.38 MB
- Runs: 0.00 MB
- Total: 14.28 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
