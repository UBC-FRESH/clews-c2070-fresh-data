# WS4 tiled 30-m dataset — I6|AB|S22

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `I6|AB|S22` (parent `I6|AB`)
- Tile / row / col: `I6` / 2 / 2
- Province: `AB`
- Centroid: 54.201241, -119.542225
- Allocated harvest: 172544.663533 m3
- Productive subcell area: 212900.022051 ha
- Committed geometry area: 248255.687817 ha
- Clipped inventory geometry: 248255.687817 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2547200
- Blocks: 1048592
- Forest area: 229248.00 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 101265
- Scheduled area: 21453.84 ha
- Eligible blocks (age class >= 40): 1012648
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 33.70 MB
- Schedules: 1.21 MB
- Runs: 0.00 MB
- Total: 34.91 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
