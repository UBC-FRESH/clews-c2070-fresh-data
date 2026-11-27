# WS4 tiled 30-m dataset — C27|QC|S32

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `C27|QC|S32` (parent `C27|QC`)
- Tile / row / col: `C27` / 3 / 2
- Province: `QC`
- Centroid: 46.765228, -73.666155
- Allocated harvest: 126873.959371 m3
- Productive subcell area: 213887.146714 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2413066
- Blocks: 832504
- Forest area: 217175.94 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 74061
- Scheduled area: 17467.47 ha
- Eligible blocks (age class >= 40): 740610
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 29.40 MB
- Schedules: 0.88 MB
- Runs: 0.00 MB
- Total: 30.28 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
