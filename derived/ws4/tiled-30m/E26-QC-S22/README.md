# WS4 tiled 30-m dataset — E26|QC|S22

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `E26|QC|S22` (parent `E26|QC`)
- Tile / row / col: `E26` / 2 / 2
- Province: `QC`
- Centroid: 49.319000, -74.483558
- Allocated harvest: 63415.489007 m3
- Productive subcell area: 175039.054875 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2041162
- Blocks: 651684
- Forest area: 183704.58 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 48923
- Scheduled area: 11347.47 ha
- Eligible blocks (age class >= 40): 489226
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 23.72 MB
- Schedules: 0.58 MB
- Runs: 0.00 MB
- Total: 24.30 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
