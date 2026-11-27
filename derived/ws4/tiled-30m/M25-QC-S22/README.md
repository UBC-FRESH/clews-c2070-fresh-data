# WS4 tiled 30-m dataset — M25|QC|S22

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `M25|QC|S22` (parent `M25|QC`)
- Tile / row / col: `M25` / 2 / 2
- Province: `QC`
- Centroid: 60.079316, -70.111426
- Allocated harvest: 5.483010 m3
- Productive subcell area: 42.842919 ha
- Committed geometry area: 232238.229395 ha
- Clipped inventory geometry: 232238.229395 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1350
- Blocks: 1139
- Forest area: 121.50 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 40
- Scheduled area: 3.69 ha
- Eligible blocks (age class >= 40): 40
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 0.10 MB
- Schedules: 0.00 MB
- Runs: 0.00 MB
- Total: 0.10 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
