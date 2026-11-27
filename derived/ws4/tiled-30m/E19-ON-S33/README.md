# WS4 tiled 30-m dataset — E19|ON|S33

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `E19|ON|S33` (parent `E19|ON`)
- Tile / row / col: `E19` / 3 / 3
- Province: `ON`
- Centroid: 51.699988, -88.209440
- Allocated harvest: 41545.087168 m3
- Productive subcell area: 202173.746580 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2272669
- Blocks: 782971
- Forest area: 204540.21 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 73653
- Scheduled area: 17694.63 ha
- Eligible blocks (age class >= 40): 736528
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 27.08 MB
- Schedules: 0.87 MB
- Runs: 0.00 MB
- Total: 27.95 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
