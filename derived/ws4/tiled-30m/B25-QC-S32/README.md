# WS4 tiled 30-m dataset — B25|QC|S32

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `B25|QC|S32` (parent `B25|QC`)
- Tile / row / col: `B25` / 3 / 2
- Province: `QC`
- Centroid: 46.365658, -77.907093
- Allocated harvest: 73834.722197 m3
- Productive subcell area: 131810.892685 ha
- Committed geometry area: 154984.049776 ha
- Clipped inventory geometry: 154984.049776 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1569347
- Blocks: 469422
- Forest area: 141241.23 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 45343
- Scheduled area: 13585.95 ha
- Eligible blocks (age class >= 40): 453429
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 18.50 MB
- Schedules: 0.53 MB
- Runs: 0.00 MB
- Total: 19.03 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
