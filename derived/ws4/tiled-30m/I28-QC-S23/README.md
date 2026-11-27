# WS4 tiled 30-m dataset — I28|QC|S23

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `I28|QC|S23` (parent `I28|QC`)
- Tile / row / col: `I28` / 2 / 3
- Province: `QC`
- Centroid: 52.964382, -66.463521
- Allocated harvest: 1735.786306 m3
- Productive subcell area: 11309.470534 ha
- Committed geometry area: 19100.320713 ha
- Clipped inventory geometry: 19100.320713 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 126256
- Blocks: 50993
- Forest area: 11363.04 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 4781
- Scheduled area: 1079.46 ha
- Eligible blocks (age class >= 40): 47806
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 2.10 MB
- Schedules: 0.05 MB
- Runs: 0.00 MB
- Total: 2.15 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
