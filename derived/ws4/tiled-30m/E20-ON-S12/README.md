# WS4 tiled 30-m dataset — E20|ON|S12

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `E20|ON|S12` (parent `E20|ON`)
- Tile / row / col: `E20` / 1 / 2
- Province: `ON`
- Centroid: 50.694567, -86.945079
- Allocated harvest: 29876.809935 m3
- Productive subcell area: 192198.875528 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2387114
- Blocks: 850383
- Forest area: 214840.26 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 73451
- Scheduled area: 16452.09 ha
- Eligible blocks (age class >= 40): 734507
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 29.12 MB
- Schedules: 0.87 MB
- Runs: 0.00 MB
- Total: 29.99 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
