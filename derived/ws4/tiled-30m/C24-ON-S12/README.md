# WS4 tiled 30-m dataset — C24|ON|S12

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `C24|ON|S12` (parent `C24|ON`)
- Tile / row / col: `C24` / 1 / 2
- Province: `ON`
- Centroid: 47.042102, -79.684970
- Allocated harvest: 52121.548839 m3
- Productive subcell area: 184542.225985 ha
- Committed geometry area: 225124.370043 ha
- Clipped inventory geometry: 225124.370043 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2113737
- Blocks: 835438
- Forest area: 190236.33 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 79904
- Scheduled area: 17551.35 ha
- Eligible blocks (age class >= 40): 799039
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 27.11 MB
- Schedules: 0.95 MB
- Runs: 0.00 MB
- Total: 28.06 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
