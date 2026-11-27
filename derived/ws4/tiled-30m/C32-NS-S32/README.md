# WS4 tiled 30-m dataset — C32|NS|S32

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `C32|NS|S32` (parent `C32|NS`)
- Tile / row / col: `C32` / 3 / 2
- Province: `NS`
- Centroid: 44.149891, -64.976268
- Allocated harvest: 124074.800264 m3
- Productive subcell area: 206603.360475 ha
- Committed geometry area: 247934.979909 ha
- Clipped inventory geometry: 247934.979909 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2219903
- Blocks: 902544
- Forest area: 199791.27 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 81731
- Scheduled area: 16362.27 ha
- Eligible blocks (age class >= 40): 817306
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 28.81 MB
- Schedules: 0.97 MB
- Runs: 0.00 MB
- Total: 29.79 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
