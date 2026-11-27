# WS4 tiled 30-m dataset — C20|ON|S21

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `C20|ON|S21` (parent `C20|ON`)
- Tile / row / col: `C20` / 2 / 1
- Province: `ON`
- Centroid: 48.666961, -88.220291
- Allocated harvest: 7717.455723 m3
- Productive subcell area: 27092.493212 ha
- Committed geometry area: 32136.812470 ha
- Clipped inventory geometry: 32136.812470 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 334304
- Blocks: 133678
- Forest area: 30087.36 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 13069
- Scheduled area: 2840.04 ha
- Eligible blocks (age class >= 40): 130688
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 5.11 MB
- Schedules: 0.15 MB
- Runs: 0.00 MB
- Total: 5.25 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
