# WS4 tiled 30-m dataset — L7|BC|S22

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `L7|BC|S22` (parent `L7|BC`)
- Tile / row / col: `L7` / 2 / 2
- Province: `BC`
- Centroid: 58.538055, -120.254092
- Allocated harvest: 52567.523674 m3
- Productive subcell area: 128546.249491 ha
- Committed geometry area: 150079.300170 ha
- Clipped inventory geometry: 150079.300170 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1234725
- Blocks: 493798
- Forest area: 111125.25 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 39430
- Scheduled area: 6314.49 ha
- Eligible blocks (age class >= 40): 394295
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 15.76 MB
- Schedules: 0.46 MB
- Runs: 0.00 MB
- Total: 16.22 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
