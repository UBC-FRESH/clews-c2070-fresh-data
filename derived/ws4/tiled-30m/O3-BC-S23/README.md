# WS4 tiled 30-m dataset — O3|BC|S23

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `O3|BC|S23` (parent `O3|BC`)
- Tile / row / col: `O3` / 2 / 3
- Province: `BC`
- Centroid: 59.787164, -132.642931
- Allocated harvest: 51699.590998 m3
- Productive subcell area: 127009.668564 ha
- Committed geometry area: 229107.153961 ha
- Clipped inventory geometry: 229107.153961 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1716517
- Blocks: 959008
- Forest area: 154486.53 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 93190
- Scheduled area: 14786.55 ha
- Eligible blocks (age class >= 40): 931893
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 25.40 MB
- Schedules: 1.11 MB
- Runs: 0.00 MB
- Total: 26.50 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
