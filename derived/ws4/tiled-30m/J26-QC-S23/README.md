# WS4 tiled 30-m dataset — J26|QC|S23

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `J26|QC|S23` (parent `J26|QC`)
- Tile / row / col: `J26` / 2 / 3
- Province: `QC`
- Centroid: 55.547649, -69.868415
- Allocated harvest: 13507.774698 m3
- Productive subcell area: 127798.873441 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1684910
- Blocks: 741509
- Forest area: 151641.90 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 61388
- Scheduled area: 13277.52 ha
- Eligible blocks (age class >= 40): 613879
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 22.33 MB
- Schedules: 0.73 MB
- Runs: 0.00 MB
- Total: 23.05 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
