# WS4 tiled 30-m dataset — K27|QC|S21

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `K27|QC|S21` (parent `K27|QC`)
- Tile / row / col: `K27` / 2 / 1
- Province: `QC`
- Centroid: 56.628636, -68.136542
- Allocated harvest: 23558.116098 m3
- Productive subcell area: 144369.027546 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2079187
- Blocks: 1142946
- Forest area: 187126.83 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 108501
- Scheduled area: 17472.96 ha
- Eligible blocks (age class >= 40): 1085008
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 30.19 MB
- Schedules: 1.30 MB
- Runs: 0.00 MB
- Total: 31.49 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
