# WS4 tiled 30-m dataset — D24|ON|S12

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `D24|ON|S12` (parent `D24|ON`)
- Tile / row / col: `D24` / 1 / 2
- Province: `ON`
- Centroid: 48.241376, -79.537798
- Allocated harvest: 794.144916 m3
- Productive subcell area: 3822.243813 ha
- Committed geometry area: 4272.707747 ha
- Clipped inventory geometry: 4272.707747 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 41586
- Blocks: 17507
- Forest area: 3742.74 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 1531
- Scheduled area: 270.45 ha
- Eligible blocks (age class >= 40): 15309
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 0.74 MB
- Schedules: 0.02 MB
- Runs: 0.00 MB
- Total: 0.76 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
