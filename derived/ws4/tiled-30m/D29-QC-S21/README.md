# WS4 tiled 30-m dataset — D29|QC|S21

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `D29|QC|S21` (parent `D29|QC`)
- Tile / row / col: `D29` / 2 / 1
- Province: `QC`
- Centroid: 46.818142, -70.198933
- Allocated harvest: 119717.841194 m3
- Productive subcell area: 208870.499967 ha
- Committed geometry area: 225990.080559 ha
- Clipped inventory geometry: 225990.080559 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2315288
- Blocks: 852645
- Forest area: 208375.92 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 75010
- Scheduled area: 17704.80 ha
- Eligible blocks (age class >= 40): 750096
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 28.61 MB
- Schedules: 0.89 MB
- Runs: 0.00 MB
- Total: 29.50 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
