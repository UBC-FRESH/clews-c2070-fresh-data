# WS4 tiled 30-m dataset — N6|YT|S33

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `N6|YT|S33` (parent `N6|YT`)
- Tile / row / col: `N6` / 3 / 3
- Province: `YT`
- Centroid: 60.880281, -124.623848
- Allocated harvest: 29.994591 m3
- Productive subcell area: 12630.654832 ha
- Committed geometry area: 14589.534126 ha
- Clipped inventory geometry: 14589.534126 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 68448
- Blocks: 40340
- Forest area: 6160.32 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 3373
- Scheduled area: 493.47 ha
- Eligible blocks (age class >= 40): 33721
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 1.40 MB
- Schedules: 0.04 MB
- Runs: 0.00 MB
- Total: 1.44 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
