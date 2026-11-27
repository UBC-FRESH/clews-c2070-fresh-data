# WS4 tiled 30-m dataset — K28|QC|S33

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `K28|QC|S33` (parent `K28|QC`)
- Tile / row / col: `K28` / 3 / 3
- Province: `QC`
- Centroid: 56.016114, -64.121790
- Allocated harvest: 12448.832060 m3
- Productive subcell area: 96645.019852 ha
- Committed geometry area: 204310.842375 ha
- Clipped inventory geometry: 204310.842375 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 579297
- Blocks: 308120
- Forest area: 52136.73 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 21313
- Scheduled area: 3252.42 ha
- Eligible blocks (age class >= 40): 213124
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 8.74 MB
- Schedules: 0.25 MB
- Runs: 0.00 MB
- Total: 8.99 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
