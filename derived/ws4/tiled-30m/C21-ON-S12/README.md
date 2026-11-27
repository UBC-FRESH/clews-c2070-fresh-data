# WS4 tiled 30-m dataset — C21|ON|S12

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `C21|ON|S12` (parent `C21|ON`)
- Tile / row / col: `C21` / 1 / 2
- Province: `ON`
- Centroid: 47.958016, -85.521141
- Allocated harvest: 20490.684001 m3
- Productive subcell area: 71568.695324 ha
- Committed geometry area: 79589.920129 ha
- Clipped inventory geometry: 79589.920129 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 838941
- Blocks: 276172
- Forest area: 75504.69 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 27132
- Scheduled area: 7401.24 ha
- Eligible blocks (age class >= 40): 271313
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 10.36 MB
- Schedules: 0.31 MB
- Runs: 0.00 MB
- Total: 10.67 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
