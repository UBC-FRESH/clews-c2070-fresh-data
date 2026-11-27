# WS4 tiled 30-m dataset — H26|QC|S21

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `H26|QC|S21` (parent `H26|QC`)
- Tile / row / col: `H26` / 2 / 1
- Province: `QC`
- Centroid: 53.320648, -73.033442
- Allocated harvest: 19944.756397 m3
- Productive subcell area: 131905.083658 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1224406
- Blocks: 358375
- Forest area: 110196.54 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 26652
- Scheduled area: 6592.77 ha
- Eligible blocks (age class >= 40): 266512
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 13.61 MB
- Schedules: 0.31 MB
- Runs: 0.00 MB
- Total: 13.93 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
