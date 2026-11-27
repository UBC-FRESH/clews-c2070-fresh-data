# WS4 tiled 30-m dataset — B23|ON|S13

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `B23|ON|S13` (parent `B23|ON`)
- Tile / row / col: `B23` / 1 / 3
- Province: `ON`
- Centroid: 46.055533, -81.332227
- Allocated harvest: 30336.641877 m3
- Productive subcell area: 100370.329151 ha
- Committed geometry area: 118824.159066 ha
- Clipped inventory geometry: 118824.159066 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1133751
- Blocks: 517292
- Forest area: 102037.59 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 49471
- Scheduled area: 9730.35 ha
- Eligible blocks (age class >= 40): 494709
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 15.85 MB
- Schedules: 0.58 MB
- Runs: 0.00 MB
- Total: 16.44 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
