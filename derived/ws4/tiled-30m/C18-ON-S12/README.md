# WS4 tiled 30-m dataset — C18|ON|S12

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `C18|ON|S12` (parent `C18|ON`)
- Tile / row / col: `C18` / 1 / 2
- Province: `ON`
- Centroid: 48.290319, -91.441681
- Allocated harvest: 34315.580387 m3
- Productive subcell area: 158634.087431 ha
- Committed geometry area: 199608.900309 ha
- Clipped inventory geometry: 199608.900309 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1648535
- Blocks: 664705
- Forest area: 148368.15 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 59306
- Scheduled area: 11233.44 ha
- Eligible blocks (age class >= 40): 593060
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 21.17 MB
- Schedules: 0.70 MB
- Runs: 0.00 MB
- Total: 21.88 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
