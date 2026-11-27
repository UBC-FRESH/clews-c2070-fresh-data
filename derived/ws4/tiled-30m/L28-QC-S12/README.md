# WS4 tiled 30-m dataset — L28|QC|S12

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `L28|QC|S12` (parent `L28|QC`)
- Tile / row / col: `L28` / 1 / 2
- Province: `QC`
- Centroid: 56.648791, -64.444753
- Allocated harvest: 4320.532081 m3
- Productive subcell area: 24632.249954 ha
- Committed geometry area: 229146.363446 ha
- Clipped inventory geometry: 229146.363446 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 112096
- Blocks: 58966
- Forest area: 10088.64 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 2491
- Scheduled area: 464.04 ha
- Eligible blocks (age class >= 40): 24908
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 2.08 MB
- Schedules: 0.03 MB
- Runs: 0.00 MB
- Total: 2.11 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
