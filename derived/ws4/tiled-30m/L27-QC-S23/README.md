# WS4 tiled 30-m dataset — L27|QC|S23

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `L27|QC|S23` (parent `L27|QC`)
- Tile / row / col: `L27` / 2 / 3
- Province: `QC`
- Centroid: 57.480989, -65.527107
- Allocated harvest: 14919.959864 m3
- Productive subcell area: 91923.631808 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 465973
- Blocks: 240469
- Forest area: 41937.57 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 15529
- Scheduled area: 2683.35 ha
- Eligible blocks (age class >= 40): 155286
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 7.25 MB
- Schedules: 0.18 MB
- Runs: 0.00 MB
- Total: 7.42 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
