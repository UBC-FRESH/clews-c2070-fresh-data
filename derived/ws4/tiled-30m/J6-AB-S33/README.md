# WS4 tiled 30-m dataset — J6|AB|S33

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `J6|AB|S33` (parent `J6|AB`)
- Tile / row / col: `J6` / 3 / 3
- Province: `AB`
- Centroid: 56.083185, -119.809594
- Allocated harvest: 49905.904603 m3
- Productive subcell area: 69730.914393 ha
- Committed geometry area: 118369.422698 ha
- Clipped inventory geometry: 118369.422698 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 549928
- Blocks: 181930
- Forest area: 49493.52 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 15814
- Scheduled area: 4592.52 ha
- Eligible blocks (age class >= 40): 158132
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 7.11 MB
- Schedules: 0.18 MB
- Runs: 0.00 MB
- Total: 7.29 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
