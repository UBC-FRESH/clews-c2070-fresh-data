# WS4 tiled 30-m dataset — M25|QC|S11

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `M25|QC|S11` (parent `M25|QC`)
- Tile / row / col: `M25` / 1 / 1
- Province: `QC`
- Centroid: 59.823145, -71.276201
- Allocated harvest: 5.902355 m3
- Productive subcell area: 46.119580 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 7464
- Blocks: 5003
- Forest area: 671.76 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 920
- Scheduled area: 111.24 ha
- Eligible blocks (age class >= 40): 920
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 0.21 MB
- Schedules: 0.01 MB
- Runs: 0.00 MB
- Total: 0.22 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
