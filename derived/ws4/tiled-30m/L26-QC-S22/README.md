# WS4 tiled 30-m dataset — L26|QC|S22

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `L26|QC|S22` (parent `L26|QC`)
- Tile / row / col: `L26` / 2 / 2
- Province: `QC`
- Centroid: 58.262984, -68.657286
- Allocated harvest: 16183.659069 m3
- Productive subcell area: 92638.290781 ha
- Committed geometry area: 249081.582813 ha
- Clipped inventory geometry: 249081.582813 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 610209
- Blocks: 367428
- Forest area: 54918.81 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 26315
- Scheduled area: 3588.48 ha
- Eligible blocks (age class >= 40): 263150
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 9.69 MB
- Schedules: 0.31 MB
- Runs: 0.00 MB
- Total: 10.00 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
