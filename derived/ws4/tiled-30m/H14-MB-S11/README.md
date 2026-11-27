# WS4 tiled 30-m dataset — H14|MB|S11

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `H14|MB|S11` (parent `H14|MB`)
- Tile / row / col: `H14` / 1 / 1
- Province: `MB`
- Centroid: 54.946740, -101.147378
- Allocated harvest: 8053.944618 m3
- Productive subcell area: 196705.864056 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1447304
- Blocks: 328385
- Forest area: 130257.36 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 20799
- Scheduled area: 3647.88 ha
- Eligible blocks (age class >= 40): 207990
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 14.65 MB
- Schedules: 0.24 MB
- Runs: 0.00 MB
- Total: 14.89 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
