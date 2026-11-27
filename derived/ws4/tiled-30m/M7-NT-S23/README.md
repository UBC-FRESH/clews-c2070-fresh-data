# WS4 tiled 30-m dataset — M7|NT|S23

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `M7|NT|S23` (parent `M7|NT`)
- Tile / row / col: `M7` / 2 / 3
- Province: `NT`
- Centroid: 60.113764, -120.317553
- Allocated harvest: 134.846133 m3
- Productive subcell area: 85695.627473 ha
- Committed geometry area: 125719.257209 ha
- Clipped inventory geometry: 125719.257209 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 653809
- Blocks: 157500
- Forest area: 58842.81 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 8497
- Scheduled area: 1446.30 ha
- Eligible blocks (age class >= 40): 84969
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 7.03 MB
- Schedules: 0.10 MB
- Runs: 0.00 MB
- Total: 7.13 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
