# WS4 tiled 30-m dataset — C27|QC|S23

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `C27|QC|S23` (parent `C27|QC`)
- Tile / row / col: `C27` / 2 / 3
- Province: `QC`
- Centroid: 46.201955, -73.282882
- Allocated harvest: 121119.945986 m3
- Productive subcell area: 204186.893713 ha
- Committed geometry area: 238661.949595 ha
- Clipped inventory geometry: 238661.949595 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1435216
- Blocks: 454217
- Forest area: 129169.44 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 36832
- Scheduled area: 11084.22 ha
- Eligible blocks (age class >= 40): 368315
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 17.20 MB
- Schedules: 0.43 MB
- Runs: 0.00 MB
- Total: 17.64 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
