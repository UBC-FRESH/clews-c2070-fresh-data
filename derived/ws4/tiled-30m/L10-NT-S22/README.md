# WS4 tiled 30-m dataset — L10|NT|S22

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `L10|NT|S22` (parent `L10|NT`)
- Tile / row / col: `L10` / 2 / 2
- Province: `NT`
- Centroid: 60.071810, -112.439449
- Allocated harvest: 73.645415 m3
- Productive subcell area: 46105.982048 ha
- Committed geometry area: 74559.502394 ha
- Clipped inventory geometry: 74559.502394 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 554009
- Blocks: 204388
- Forest area: 49860.81 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 15358
- Scheduled area: 5218.83 ha
- Eligible blocks (age class >= 40): 153574
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 7.37 MB
- Schedules: 0.18 MB
- Runs: 0.00 MB
- Total: 7.54 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
