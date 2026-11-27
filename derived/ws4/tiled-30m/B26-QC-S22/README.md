# WS4 tiled 30-m dataset — B26|QC|S22

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `B26|QC|S22` (parent `B26|QC`)
- Tile / row / col: `B26` / 2 / 2
- Province: `QC`
- Centroid: 45.599552, -76.263425
- Allocated harvest: 58423.064723 m3
- Productive subcell area: 96882.737870 ha
- Committed geometry area: 120343.539370 ha
- Clipped inventory geometry: 120343.539370 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 865326
- Blocks: 266509
- Forest area: 77879.34 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 23352
- Scheduled area: 7071.66 ha
- Eligible blocks (age class >= 40): 233514
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 10.44 MB
- Schedules: 0.27 MB
- Runs: 0.00 MB
- Total: 10.71 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
