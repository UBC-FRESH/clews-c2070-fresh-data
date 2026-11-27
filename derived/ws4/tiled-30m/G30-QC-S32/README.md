# WS4 tiled 30-m dataset — G30|QC|S32

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `G30|QC|S32` (parent `G30|QC`)
- Tile / row / col: `G30` / 3 / 2
- Province: `QC`
- Centroid: 50.329371, -64.924257
- Allocated harvest: 15399.632737 m3
- Productive subcell area: 34709.892103 ha
- Committed geometry area: 39828.364499 ha
- Clipped inventory geometry: 39828.364499 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 345943
- Blocks: 143863
- Forest area: 31134.87 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 13189
- Scheduled area: 3187.80 ha
- Eligible blocks (age class >= 40): 131883
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 5.30 MB
- Schedules: 0.15 MB
- Runs: 0.00 MB
- Total: 5.45 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
