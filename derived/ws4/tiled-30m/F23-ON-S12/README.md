# WS4 tiled 30-m dataset — F23|ON|S12

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `F23|ON|S12` (parent `F23|ON`)
- Tile / row / col: `F23` / 1 / 2
- Province: `ON`
- Centroid: 51.210917, -80.285110
- Allocated harvest: 5816.750892 m3
- Productive subcell area: 88408.369890 ha
- Committed geometry area: 128841.327829 ha
- Clipped inventory geometry: 128841.327829 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 848531
- Blocks: 358794
- Forest area: 76367.79 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 32927
- Scheduled area: 7337.34 ha
- Eligible blocks (age class >= 40): 329270
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 11.47 MB
- Schedules: 0.39 MB
- Runs: 0.00 MB
- Total: 11.85 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
