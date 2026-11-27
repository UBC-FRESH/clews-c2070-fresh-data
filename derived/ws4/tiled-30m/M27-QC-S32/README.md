# WS4 tiled 30-m dataset — M27|QC|S32

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `M27|QC|S32` (parent `M27|QC`)
- Tile / row / col: `M27` / 3 / 2
- Province: `QC`
- Centroid: 59.307509, -64.825730
- Allocated harvest: 2489.886378 m3
- Productive subcell area: 13592.276804 ha
- Committed geometry area: 174173.088622 ha
- Clipped inventory geometry: 174173.088622 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 46255
- Blocks: 25258
- Forest area: 4162.95 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 1125
- Scheduled area: 158.67 ha
- Eligible blocks (age class >= 40): 11244
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 0.90 MB
- Schedules: 0.01 MB
- Runs: 0.00 MB
- Total: 0.91 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
