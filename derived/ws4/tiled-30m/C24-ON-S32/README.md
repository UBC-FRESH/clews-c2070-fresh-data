# WS4 tiled 30-m dataset — C24|ON|S32

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `C24|ON|S32` (parent `C24|ON`)
- Tile / row / col: `C24` / 3 / 2
- Province: `ON`
- Centroid: 47.918809, -79.595454
- Allocated harvest: 12508.625734 m3
- Productive subcell area: 44288.201105 ha
- Committed geometry area: 54027.490570 ha
- Clipped inventory geometry: 54027.490570 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 520292
- Blocks: 214923
- Forest area: 46826.28 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 20174
- Scheduled area: 3985.56 ha
- Eligible blocks (age class >= 40): 201740
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 7.47 MB
- Schedules: 0.23 MB
- Runs: 0.00 MB
- Total: 7.70 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
