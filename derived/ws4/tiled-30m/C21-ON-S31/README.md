# WS4 tiled 30-m dataset — C21|ON|S31

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `C21|ON|S31` (parent `C21|ON`)
- Tile / row / col: `C21` / 3 / 1
- Province: `ON`
- Centroid: 48.786862, -85.939349
- Allocated harvest: 64307.410178 m3
- Productive subcell area: 224609.263694 ha
- Committed geometry area: 249782.859343 ha
- Clipped inventory geometry: 249782.859343 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2498832
- Blocks: 924346
- Forest area: 224894.88 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 84950
- Scheduled area: 19769.04 ha
- Eligible blocks (age class >= 40): 849500
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 31.22 MB
- Schedules: 1.01 MB
- Runs: 0.00 MB
- Total: 32.23 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
