# WS4 tiled 30-m dataset — M10|NT|S32

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `M10|NT|S32` (parent `M10|NT`)
- Tile / row / col: `M10` / 3 / 2
- Province: `NT`
- Centroid: 61.686055, -113.477887
- Allocated harvest: 165.218418 m3
- Productive subcell area: 123265.143318 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 64407
- Blocks: 31701
- Forest area: 5796.63 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 2929
- Scheduled area: 562.50 ha
- Eligible blocks (age class >= 40): 29285
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 1.20 MB
- Schedules: 0.03 MB
- Runs: 0.00 MB
- Total: 1.23 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
