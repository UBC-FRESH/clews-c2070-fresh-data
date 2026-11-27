# WS4 tiled 30-m dataset — M10|NT|S22

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `M10|NT|S22` (parent `M10|NT`)
- Tile / row / col: `M10` / 2 / 2
- Province: `NT`
- Centroid: 61.242850, -113.203119
- Allocated harvest: 165.218418 m3
- Productive subcell area: 123265.143318 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1984491
- Blocks: 1025823
- Forest area: 178604.19 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 94916
- Scheduled area: 16517.97 ha
- Eligible blocks (age class >= 40): 949158
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 28.15 MB
- Schedules: 1.13 MB
- Runs: 0.00 MB
- Total: 29.28 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
