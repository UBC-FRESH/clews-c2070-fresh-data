# WS4 tiled 30-m dataset — J23|QC|S33

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `J23|QC|S33` (parent `J23|QC`)
- Tile / row / col: `J23` / 3 / 3
- Province: `QC`
- Centroid: 57.388984, -76.458977
- Allocated harvest: 1688.373119 m3
- Productive subcell area: 12158.371439 ha
- Committed geometry area: 145485.245506 ha
- Clipped inventory geometry: 145485.245506 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 205079
- Blocks: 116572
- Forest area: 18457.11 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 5295
- Scheduled area: 754.74 ha
- Eligible blocks (age class >= 40): 52942
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 3.80 MB
- Schedules: 0.06 MB
- Runs: 0.00 MB
- Total: 3.86 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
