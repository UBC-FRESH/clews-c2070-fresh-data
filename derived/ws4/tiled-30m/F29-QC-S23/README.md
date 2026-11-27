# WS4 tiled 30-m dataset — F29|QC|S23

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `F29|QC|S23` (parent `F29|QC`)
- Tile / row / col: `F29` / 2 / 3
- Province: `QC`
- Centroid: 48.806217, -67.276404
- Allocated harvest: 44280.497727 m3
- Productive subcell area: 96145.189927 ha
- Committed geometry area: 114524.472027 ha
- Clipped inventory geometry: 114524.472027 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1056630
- Blocks: 374664
- Forest area: 95096.70 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 32281
- Scheduled area: 7895.34 ha
- Eligible blocks (age class >= 40): 322801
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 13.01 MB
- Schedules: 0.38 MB
- Runs: 0.00 MB
- Total: 13.38 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
