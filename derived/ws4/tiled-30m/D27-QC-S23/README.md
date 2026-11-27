# WS4 tiled 30-m dataset — D27|QC|S23

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `D27|QC|S23` (parent `D27|QC`)
- Tile / row / col: `D27` / 2 / 3
- Province: `QC`
- Centroid: 47.455231, -72.610119
- Allocated harvest: 120307.451326 m3
- Productive subcell area: 223494.001956 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2400019
- Blocks: 878706
- Forest area: 216001.71 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 77852
- Scheduled area: 16903.53 ha
- Eligible blocks (age class >= 40): 778516
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 29.99 MB
- Schedules: 0.92 MB
- Runs: 0.00 MB
- Total: 30.92 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
