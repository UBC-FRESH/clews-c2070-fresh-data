# WS4 tiled 30-m dataset — C32|NS|S11

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `C32|NS|S11` (parent `C32|NS`)
- Tile / row / col: `C32` / 1 / 1
- Province: `NS`
- Centroid: 43.602290, -65.738450
- Allocated harvest: 12953.370233 m3
- Productive subcell area: 21569.326034 ha
- Committed geometry area: 25884.334140 ha
- Clipped inventory geometry: 25884.334140 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 193109
- Blocks: 64537
- Forest area: 17379.81 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 5677
- Scheduled area: 1528.20 ha
- Eligible blocks (age class >= 40): 56765
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 2.82 MB
- Schedules: 0.06 MB
- Runs: 0.00 MB
- Total: 2.88 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
