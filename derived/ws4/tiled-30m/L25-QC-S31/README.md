# WS4 tiled 30-m dataset — L25|QC|S31

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `L25|QC|S31` (parent `L25|QC`)
- Tile / row / col: `L25` / 3 / 1
- Province: `QC`
- Centroid: 59.392936, -71.605836
- Allocated harvest: 908.419413 m3
- Productive subcell area: 6964.015037 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 14120
- Blocks: 12729
- Forest area: 1270.80 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 392
- Scheduled area: 36.63 ha
- Eligible blocks (age class >= 40): 392
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 0.39 MB
- Schedules: 0.00 MB
- Runs: 0.00 MB
- Total: 0.39 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
