# WS4 tiled 30-m dataset — H32|QC|S31

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `H32|QC|S31` (parent `H32|QC`)
- Tile / row / col: `H32` / 3 / 1
- Province: `QC`
- Centroid: 50.326983, -60.791483
- Allocated harvest: 19890.938897 m3
- Productive subcell area: 70885.331024 ha
- Committed geometry area: 131578.741382 ha
- Clipped inventory geometry: 131578.741382 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 684088
- Blocks: 299848
- Forest area: 61567.92 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 26231
- Scheduled area: 5535.63 ha
- Eligible blocks (age class >= 40): 262303
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 9.53 MB
- Schedules: 0.30 MB
- Runs: 0.00 MB
- Total: 9.83 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
