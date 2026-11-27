# WS4 tiled 30-m dataset — E16|ON|S13

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `E16|ON|S13` (parent `E16|ON`)
- Tile / row / col: `E16` / 1 / 3
- Province: `ON`
- Centroid: 51.017966, -94.795770
- Allocated harvest: 29774.598885 m3
- Productive subcell area: 168342.867764 ha
- Committed geometry area: 248635.839786 ha
- Clipped inventory geometry: 248635.839786 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1389848
- Blocks: 452517
- Forest area: 125086.32 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 24447
- Scheduled area: 4046.04 ha
- Eligible blocks (age class >= 40): 244465
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 16.11 MB
- Schedules: 0.29 MB
- Runs: 0.00 MB
- Total: 16.40 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
