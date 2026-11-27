# WS4 tiled 30-m dataset — K6|BC|S22

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `K6|BC|S22` (parent `K6|BC`)
- Tile / row / col: `K6` / 2 / 2
- Province: `BC`
- Centroid: 56.733972, -121.433720
- Allocated harvest: 98740.202921 m3
- Productive subcell area: 214208.343932 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2402691
- Blocks: 1126533
- Forest area: 216242.19 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 101345
- Scheduled area: 17160.93 ha
- Eligible blocks (age class >= 40): 1013448
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 32.93 MB
- Schedules: 1.22 MB
- Runs: 0.00 MB
- Total: 34.14 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
