# WS4 tiled 30-m dataset — K27|QC|S13

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `K27|QC|S13` (parent `K27|QC`)
- Tile / row / col: `K27` / 1 / 3
- Province: `QC`
- Centroid: 55.827761, -66.984016
- Allocated harvest: 23558.116098 m3
- Productive subcell area: 144369.027546 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1750692
- Blocks: 997579
- Forest area: 157562.28 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 92392
- Scheduled area: 15186.06 ha
- Eligible blocks (age class >= 40): 923918
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 25.78 MB
- Schedules: 1.10 MB
- Runs: 0.00 MB
- Total: 26.88 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
