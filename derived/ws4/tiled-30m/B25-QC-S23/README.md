# WS4 tiled 30-m dataset — B25|QC|S23

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `B25|QC|S23` (parent `B25|QC`)
- Tile / row / col: `B25` / 2 / 3
- Province: `QC`
- Centroid: 45.880570, -77.162339
- Allocated harvest: 2019.993099 m3
- Productive subcell area: 3606.123049 ha
- Committed geometry area: 4240.101427 ha
- Clipped inventory geometry: 4240.101427 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 22080
- Blocks: 7821
- Forest area: 1987.20 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 673
- Scheduled area: 156.69 ha
- Eligible blocks (age class >= 40): 6721
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 0.40 MB
- Schedules: 0.01 MB
- Runs: 0.00 MB
- Total: 0.41 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
