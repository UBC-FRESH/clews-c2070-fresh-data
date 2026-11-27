# WS4 tiled 30-m dataset — I25|QC|S12

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `I25|QC|S12` (parent `I25|QC`)
- Tile / row / col: `I25` / 1 / 2
- Province: `QC`
- Centroid: 54.484916, -73.979681
- Allocated harvest: 15858.451832 m3
- Productive subcell area: 122379.864931 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1299883
- Blocks: 369648
- Forest area: 116989.47 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 29577
- Scheduled area: 6380.10 ha
- Eligible blocks (age class >= 40): 295770
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 14.04 MB
- Schedules: 0.35 MB
- Runs: 0.00 MB
- Total: 14.39 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
