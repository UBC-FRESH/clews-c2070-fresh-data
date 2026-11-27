# WS4 tiled 30-m dataset — C29|QC|S22

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `C29|QC|S22` (parent `C29|QC`)
- Tile / row / col: `C29` / 2 / 2
- Province: `QC`
- Centroid: 45.398422, -70.641980
- Allocated harvest: 426.099811 m3
- Productive subcell area: 742.292816 ha
- Committed geometry area: 734.257911 ha
- Clipped inventory geometry: 734.257911 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 6999
- Blocks: 2116
- Forest area: 629.91 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 2110
- Scheduled area: 626.67 ha
- Eligible blocks (age class >= 40): 2110
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 0.17 MB
- Schedules: 0.02 MB
- Runs: 0.00 MB
- Total: 0.19 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
