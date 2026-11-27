# WS4 tiled 30-m dataset — F29|QC|S21

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `F29|QC|S21` (parent `F29|QC`)
- Tile / row / col: `F29` / 2 / 1
- Province: `QC`
- Centroid: 49.290138, -68.606500
- Allocated harvest: 92852.916800 m3
- Productive subcell area: 201609.326433 ha
- Committed geometry area: 240149.316707 ha
- Clipped inventory geometry: 240149.316707 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2313504
- Blocks: 751524
- Forest area: 208215.36 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 64097
- Scheduled area: 16521.84 ha
- Eligible blocks (age class >= 40): 640966
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 26.94 MB
- Schedules: 0.76 MB
- Runs: 0.00 MB
- Total: 27.70 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
