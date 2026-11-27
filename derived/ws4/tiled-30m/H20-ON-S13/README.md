# WS4 tiled 30-m dataset — H20|ON|S13

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `H20|ON|S13` (parent `H20|ON`)
- Tile / row / col: `H20` / 1 / 3
- Province: `ON`
- Centroid: 54.686570, -85.264020
- Allocated harvest: 6398.118908 m3
- Productive subcell area: 112765.261230 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1187709
- Blocks: 542048
- Forest area: 106893.81 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 44492
- Scheduled area: 8848.17 ha
- Eligible blocks (age class >= 40): 444918
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 16.13 MB
- Schedules: 0.52 MB
- Runs: 0.00 MB
- Total: 16.66 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
