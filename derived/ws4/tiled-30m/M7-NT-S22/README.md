# WS4 tiled 30-m dataset — M7|NT|S22

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `M7|NT|S22` (parent `M7|NT`)
- Tile / row / col: `M7` / 2 / 2
- Province: `NT`
- Centroid: 60.041501, -121.052733
- Allocated harvest: 26.254778 m3
- Productive subcell area: 16685.088865 ha
- Committed geometry area: 24477.759723 ha
- Clipped inventory geometry: 24477.759723 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 185351
- Blocks: 31348
- Forest area: 16681.59 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 1480
- Scheduled area: 208.62 ha
- Eligible blocks (age class >= 40): 14798
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 1.97 MB
- Schedules: 0.02 MB
- Runs: 0.00 MB
- Total: 1.98 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
