# WS4 tiled 30-m dataset — L26|QC|S23

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `L26|QC|S23` (parent `L26|QC`)
- Tile / row / col: `L26` / 2 / 3
- Province: `QC`
- Centroid: 58.070810, -67.868108
- Allocated harvest: 15679.016187 m3
- Productive subcell area: 89749.620556 ha
- Committed geometry area: 241314.658945 ha
- Clipped inventory geometry: 241314.658945 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1239984
- Blocks: 692894
- Forest area: 111598.56 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 57952
- Scheduled area: 9069.21 ha
- Eligible blocks (age class >= 40): 579511
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 18.44 MB
- Schedules: 0.69 MB
- Runs: 0.00 MB
- Total: 19.13 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
