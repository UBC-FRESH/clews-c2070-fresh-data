# WS4 tiled 30-m dataset — D28|QC|S33

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `D28|QC|S33` (parent `D28|QC`)
- Tile / row / col: `D28` / 3 / 3
- Province: `QC`
- Centroid: 47.435578, -70.621516
- Allocated harvest: 73182.016355 m3
- Productive subcell area: 124795.099182 ha
- Committed geometry area: 157531.568029 ha
- Clipped inventory geometry: 157531.568029 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1513568
- Blocks: 553598
- Forest area: 136221.12 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 47891
- Scheduled area: 10592.91 ha
- Eligible blocks (age class >= 40): 478909
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 18.88 MB
- Schedules: 0.56 MB
- Runs: 0.00 MB
- Total: 19.44 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
