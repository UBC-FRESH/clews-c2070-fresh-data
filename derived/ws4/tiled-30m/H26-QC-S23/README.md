# WS4 tiled 30-m dataset — H26|QC|S23

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `H26|QC|S23` (parent `H26|QC`)
- Tile / row / col: `H26` / 2 / 3
- Province: `QC`
- Centroid: 53.002546, -71.612393
- Allocated harvest: 19944.756397 m3
- Productive subcell area: 131905.083658 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1498173
- Blocks: 447172
- Forest area: 134835.57 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 38571
- Scheduled area: 13871.61 ha
- Eligible blocks (age class >= 40): 385708
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 17.18 MB
- Schedules: 0.45 MB
- Runs: 0.00 MB
- Total: 17.64 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
