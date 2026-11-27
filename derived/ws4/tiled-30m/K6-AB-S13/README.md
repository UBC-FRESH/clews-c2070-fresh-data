# WS4 tiled 30-m dataset — K6|AB|S13

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `K6|AB|S13` (parent `K6|AB`)
- Tile / row / col: `K6` / 1 / 3
- Province: `AB`
- Centroid: 56.445028, -119.932402
- Allocated harvest: 10263.232574 m3
- Productive subcell area: 16258.236859 ha
- Committed geometry area: 21300.420392 ha
- Clipped inventory geometry: 21300.420392 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 214620
- Blocks: 97863
- Forest area: 19315.80 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 8405
- Scheduled area: 1477.98 ha
- Eligible blocks (age class >= 40): 84048
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 3.58 MB
- Schedules: 0.09 MB
- Runs: 0.00 MB
- Total: 3.67 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
