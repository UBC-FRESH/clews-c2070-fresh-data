# WS4 tiled 30-m dataset — J27|QC|S21

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `J27|QC|S21` (parent `J27|QC`)
- Tile / row / col: `J27` / 2 / 1
- Province: `QC`
- Centroid: 55.368782, -69.125876
- Allocated harvest: 17915.927235 m3
- Productive subcell area: 147541.478934 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1546716
- Blocks: 759694
- Forest area: 139204.44 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 62193
- Scheduled area: 11380.86 ha
- Eligible blocks (age class >= 40): 621927
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 21.52 MB
- Schedules: 0.74 MB
- Runs: 0.00 MB
- Total: 22.26 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
