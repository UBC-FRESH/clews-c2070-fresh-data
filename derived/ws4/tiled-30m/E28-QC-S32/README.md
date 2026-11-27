# WS4 tiled 30-m dataset — E28|QC|S32

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `E28|QC|S32` (parent `E28|QC`)
- Tile / row / col: `E28` / 3 / 2
- Province: `QC`
- Centroid: 48.803342, -70.394841
- Allocated harvest: 103517.441804 m3
- Productive subcell area: 212624.115112 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2415361
- Blocks: 817071
- Forest area: 217382.49 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 60884
- Scheduled area: 13556.43 ha
- Eligible blocks (age class >= 40): 608831
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 28.93 MB
- Schedules: 0.72 MB
- Runs: 0.00 MB
- Total: 29.66 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
