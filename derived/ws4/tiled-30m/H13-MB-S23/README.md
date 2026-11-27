# WS4 tiled 30-m dataset — H13|MB|S23

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `H13|MB|S23` (parent `H13|MB`)
- Tile / row / col: `H13` / 2 / 3
- Province: `MB`
- Centroid: 55.365263, -101.780025
- Allocated harvest: 2776.947057 m3
- Productive subcell area: 70988.684698 ha
- Committed geometry area: 96849.681619 ha
- Clipped inventory geometry: 96849.681619 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 875330
- Blocks: 193926
- Forest area: 78779.70 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 16893
- Scheduled area: 6797.16 ha
- Eligible blocks (age class >= 40): 168924
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 8.84 MB
- Schedules: 0.19 MB
- Runs: 0.00 MB
- Total: 9.04 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
