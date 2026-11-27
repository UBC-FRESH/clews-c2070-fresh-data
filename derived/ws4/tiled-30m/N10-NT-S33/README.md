# WS4 tiled 30-m dataset — N10|NT|S33

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `N10|NT|S33` (parent `N10|NT`)
- Tile / row / col: `N10` / 3 / 3
- Province: `NT`
- Centroid: 63.147899, -113.376843
- Allocated harvest: 77.839125 m3
- Productive subcell area: 101502.663044 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1739558
- Blocks: 530626
- Forest area: 156560.22 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 35341
- Scheduled area: 8116.56 ha
- Eligible blocks (age class >= 40): 353409
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 19.15 MB
- Schedules: 0.42 MB
- Runs: 0.00 MB
- Total: 19.57 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
