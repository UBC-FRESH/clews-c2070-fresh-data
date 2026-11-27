# WS4 tiled 30-m dataset — I26|QC|S21

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `I26|QC|S21` (parent `I26|QC`)
- Tile / row / col: `I26` / 2 / 1
- Province: `QC`
- Centroid: 54.606778, -72.233222
- Allocated harvest: 16708.372337 m3
- Productive subcell area: 138607.054134 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1195384
- Blocks: 490763
- Forest area: 107584.56 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 37856
- Scheduled area: 8295.75 ha
- Eligible blocks (age class >= 40): 378558
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 15.45 MB
- Schedules: 0.45 MB
- Runs: 0.00 MB
- Total: 15.90 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
