# WS4 tiled 30-m dataset — I26|QC|S23

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `I26|QC|S23` (parent `I26|QC`)
- Tile / row / col: `I26` / 2 / 3
- Province: `QC`
- Centroid: 54.276578, -70.770216
- Allocated harvest: 16708.372337 m3
- Productive subcell area: 138607.054134 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1710919
- Blocks: 508556
- Forest area: 153982.71 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 43513
- Scheduled area: 14027.76 ha
- Eligible blocks (age class >= 40): 435125
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 19.47 MB
- Schedules: 0.51 MB
- Runs: 0.00 MB
- Total: 19.98 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
