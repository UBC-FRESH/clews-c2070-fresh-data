# WS4 tiled 30-m dataset — L28|QC|S32

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `L28|QC|S32` (parent `L28|QC`)
- Tile / row / col: `L28` / 3 / 2
- Province: `QC`
- Centroid: 57.491733, -63.889880
- Allocated harvest: 1490.464248 m3
- Productive subcell area: 8497.445964 ha
- Committed geometry area: 79049.167043 ha
- Clipped inventory geometry: 79049.167043 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 659
- Blocks: 588
- Forest area: 59.31 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 84
- Scheduled area: 8.01 ha
- Eligible blocks (age class >= 40): 84
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 0.09 MB
- Schedules: 0.00 MB
- Runs: 0.00 MB
- Total: 0.09 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
