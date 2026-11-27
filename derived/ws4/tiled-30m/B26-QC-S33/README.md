# WS4 tiled 30-m dataset — B26|QC|S33

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `B26|QC|S33` (parent `B26|QC`)
- Tile / row / col: `B26` / 3 / 3
- Province: `QC`
- Centroid: 45.783559, -75.493233
- Allocated harvest: 119555.407630 m3
- Productive subcell area: 198258.261069 ha
- Committed geometry area: 246267.822018 ha
- Clipped inventory geometry: 246267.822018 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2254529
- Blocks: 590346
- Forest area: 202907.61 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 54500
- Scheduled area: 19356.75 ha
- Eligible blocks (age class >= 40): 544996
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 24.88 MB
- Schedules: 0.64 MB
- Runs: 0.00 MB
- Total: 25.52 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
