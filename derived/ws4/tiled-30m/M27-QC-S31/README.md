# WS4 tiled 30-m dataset — M27|QC|S31

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `M27|QC|S31` (parent `M27|QC`)
- Tile / row / col: `M27` / 3 / 1
- Province: `QC`
- Centroid: 59.530325, -65.289036
- Allocated harvest: 1505.457275 m3
- Productive subcell area: 8218.283444 ha
- Committed geometry area: 105310.083896 ha
- Clipped inventory geometry: 105310.083896 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 14389
- Blocks: 9483
- Forest area: 1295.01 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 3690
- Scheduled area: 468.72 ha
- Eligible blocks (age class >= 40): 3690
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 0.35 MB
- Schedules: 0.04 MB
- Runs: 0.00 MB
- Total: 0.38 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
