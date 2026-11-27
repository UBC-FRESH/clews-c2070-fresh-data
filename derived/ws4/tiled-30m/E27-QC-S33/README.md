# WS4 tiled 30-m dataset — E27|QC|S33

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `E27|QC|S33` (parent `E27|QC`)
- Tile / row / col: `E27` / 3 / 3
- Province: `QC`
- Centroid: 49.134223, -71.664658
- Allocated harvest: 84414.444630 m3
- Productive subcell area: 198894.418245 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2426692
- Blocks: 855070
- Forest area: 218402.28 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 72678
- Scheduled area: 16211.25 ha
- Eligible blocks (age class >= 40): 726779
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 29.71 MB
- Schedules: 0.86 MB
- Runs: 0.00 MB
- Total: 30.57 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
