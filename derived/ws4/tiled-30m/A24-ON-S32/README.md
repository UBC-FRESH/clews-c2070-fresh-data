# WS4 tiled 30-m dataset — A24|ON|S32

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `A24|ON|S32` (parent `A24|ON`)
- Tile / row / col: `A24` / 3 / 2
- Province: `ON`
- Centroid: 45.366778, -80.242009
- Allocated harvest: 13786.789633 m3
- Productive subcell area: 52965.561010 ha
- Committed geometry area: 110391.116456 ha
- Clipped inventory geometry: 110391.116456 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1007721
- Blocks: 405091
- Forest area: 90694.89 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 37940
- Scheduled area: 8398.08 ha
- Eligible blocks (age class >= 40): 379394
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 13.10 MB
- Schedules: 0.44 MB
- Runs: 0.00 MB
- Total: 13.55 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
