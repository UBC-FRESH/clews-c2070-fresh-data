# WS4 tiled 30-m dataset — C19|ON|S11

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `C19|ON|S11` (parent `C19|ON`)
- Tile / row / col: `C19` / 1 / 1
- Province: `ON`
- Centroid: 48.240608, -90.092417
- Allocated harvest: 38467.975743 m3
- Productive subcell area: 157629.274719 ha
- Committed geometry area: 188779.694912 ha
- Clipped inventory geometry: 188779.694912 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1834132
- Blocks: 653453
- Forest area: 165071.88 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 57383
- Scheduled area: 12183.12 ha
- Eligible blocks (age class >= 40): 573829
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 22.24 MB
- Schedules: 0.68 MB
- Runs: 0.00 MB
- Total: 22.92 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
