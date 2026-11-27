# WS4 tiled 30-m dataset — F23|QC|S23

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `F23|QC|S23` (parent `F23|QC`)
- Tile / row / col: `F23` / 2 / 3
- Province: `QC`
- Centroid: 51.522940, -79.252244
- Allocated harvest: 6450.865669 m3
- Productive subcell area: 50761.814658 ha
- Committed geometry area: 76678.713900 ha
- Clipped inventory geometry: 76678.713900 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 561800
- Blocks: 220584
- Forest area: 50562.00 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 20201
- Scheduled area: 5221.08 ha
- Eligible blocks (age class >= 40): 202006
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 7.68 MB
- Schedules: 0.23 MB
- Runs: 0.00 MB
- Total: 7.91 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
