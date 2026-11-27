# WS4 tiled 30-m dataset — J32|QC|S21

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `J32|QC|S21` (parent `J32|QC`)
- Tile / row / col: `J32` / 2 / 1
- Province: `QC`
- Centroid: 51.945325, -58.872566
- Allocated harvest: 4737.686744 m3
- Productive subcell area: 23460.907894 ha
- Committed geometry area: 33029.484387 ha
- Clipped inventory geometry: 33029.484387 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 241082
- Blocks: 72458
- Forest area: 21697.38 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 6103
- Scheduled area: 1593.63 ha
- Eligible blocks (age class >= 40): 61025
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 3.26 MB
- Schedules: 0.07 MB
- Runs: 0.00 MB
- Total: 3.33 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
