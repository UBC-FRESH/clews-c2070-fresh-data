# WS4 tiled 30-m dataset — E24|QC|S23

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `E24|QC|S23` (parent `E24|QC`)
- Tile / row / col: `E24` / 2 / 3
- Province: `QC`
- Centroid: 49.977496, -77.802837
- Allocated harvest: 35482.439363 m3
- Productive subcell area: 174007.072475 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1541289
- Blocks: 493898
- Forest area: 138716.01 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 43511
- Scheduled area: 11115.45 ha
- Eligible blocks (age class >= 40): 435108
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 18.16 MB
- Schedules: 0.51 MB
- Runs: 0.00 MB
- Total: 18.67 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
