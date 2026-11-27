# WS4 tiled 30-m dataset — R10|NT|S31

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `R10|NT|S31` (parent `R10|NT`)
- Tile / row / col: `R10` / 3 / 1
- Province: `NT`
- Centroid: 68.155509, -120.662145
- Allocated harvest: 0.078793 m3
- Productive subcell area: 225.037719 ha
- Committed geometry area: 7687.127281 ha
- Clipped inventory geometry: 7687.127281 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 507
- Blocks: 431
- Forest area: 45.63 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 21
- Scheduled area: 2.07 ha
- Eligible blocks (age class >= 40): 21
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
