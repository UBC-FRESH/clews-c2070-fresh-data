# WS4 tiled 30-m dataset — D18|ON|S23

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `D18|ON|S23` (parent `D18|ON`)
- Tile / row / col: `D18` / 2 / 3
- Province: `ON`
- Centroid: 50.015931, -90.597399
- Allocated harvest: 47213.649233 m3
- Productive subcell area: 198941.060588 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2051119
- Blocks: 647948
- Forest area: 184600.71 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 56734
- Scheduled area: 13244.04 ha
- Eligible blocks (age class >= 40): 567332
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 23.31 MB
- Schedules: 0.67 MB
- Runs: 0.00 MB
- Total: 23.98 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
