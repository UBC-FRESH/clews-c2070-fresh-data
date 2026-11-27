# WS4 tiled 30-m dataset — G10|SK|S23

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `G10|SK|S23` (parent `G10|SK`)
- Tile / row / col: `G10` / 2 / 3
- Province: `SK`
- Centroid: 53.335006, -108.598298
- Allocated harvest: 21047.038587 m3
- Productive subcell area: 87530.582817 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 645243
- Blocks: 272660
- Forest area: 58071.87 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 19061
- Scheduled area: 4396.50 ha
- Eligible blocks (age class >= 40): 190609
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 8.81 MB
- Schedules: 0.22 MB
- Runs: 0.00 MB
- Total: 9.03 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
