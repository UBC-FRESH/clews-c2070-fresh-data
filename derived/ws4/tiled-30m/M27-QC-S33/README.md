# WS4 tiled 30-m dataset — M27|QC|S33

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `M27|QC|S33` (parent `M27|QC`)
- Tile / row / col: `M27` / 3 / 3
- Province: `QC`
- Centroid: 59.034874, -64.382377
- Allocated harvest: 206.050599 m3
- Productive subcell area: 1124.829152 ha
- Committed geometry area: 14413.697602 ha
- Clipped inventory geometry: 14413.697602 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 425
- Blocks: 306
- Forest area: 38.25 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 111
- Scheduled area: 11.79 ha
- Eligible blocks (age class >= 40): 111
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 0.08 MB
- Schedules: 0.00 MB
- Runs: 0.00 MB
- Total: 0.08 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
