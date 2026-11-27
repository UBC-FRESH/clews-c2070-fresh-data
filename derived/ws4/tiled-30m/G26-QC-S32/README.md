# WS4 tiled 30-m dataset — G26|QC|S32

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `G26|QC|S32` (parent `G26|QC`)
- Tile / row / col: `G26` / 3 / 2
- Province: `QC`
- Centroid: 52.309638, -72.837724
- Allocated harvest: 38073.643729 m3
- Productive subcell area: 156354.658898 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1842510
- Blocks: 488102
- Forest area: 165825.90 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 39812
- Scheduled area: 14234.31 ha
- Eligible blocks (age class >= 40): 398116
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 19.97 MB
- Schedules: 0.47 MB
- Runs: 0.00 MB
- Total: 20.44 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
