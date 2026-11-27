# WS4 tiled 30-m dataset — H14|MB|S21

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `H14|MB|S21` (parent `H14|MB`)
- Tile / row / col: `H14` / 2 / 1
- Province: `MB`
- Centroid: 55.402565, -101.225083
- Allocated harvest: 8053.944618 m3
- Productive subcell area: 196705.864056 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1094550
- Blocks: 306968
- Forest area: 98509.50 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 23252
- Scheduled area: 7143.21 ha
- Eligible blocks (age class >= 40): 232520
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 11.87 MB
- Schedules: 0.27 MB
- Runs: 0.00 MB
- Total: 12.14 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
