# WS4 tiled 30-m dataset — C32|NS|S23

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `C32|NS|S23` (parent `C32|NS`)
- Tile / row / col: `C32` / 2 / 3
- Province: `NS`
- Centroid: 43.833127, -64.842204
- Allocated harvest: 309.693172 m3
- Productive subcell area: 515.686101 ha
- Committed geometry area: 618.850646 ha
- Clipped inventory geometry: 618.850646 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 4438
- Blocks: 2215
- Forest area: 399.42 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 1771
- Scheduled area: 328.68 ha
- Eligible blocks (age class >= 40): 1771
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 0.15 MB
- Schedules: 0.02 MB
- Runs: 0.00 MB
- Total: 0.17 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
