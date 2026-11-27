# WS4 tiled 30-m dataset — J10|SK|S23

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `J10|SK|S23` (parent `J10|SK`)
- Tile / row / col: `J10` / 2 / 3
- Province: `SK`
- Centroid: 57.354260, -109.896224
- Allocated harvest: 6297.444604 m3
- Productive subcell area: 47338.981266 ha
- Committed geometry area: 57489.088812 ha
- Clipped inventory geometry: 57489.088812 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 576513
- Blocks: 52371
- Forest area: 51886.17 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 2545
- Scheduled area: 667.08 ha
- Eligible blocks (age class >= 40): 25449
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 4.21 MB
- Schedules: 0.03 MB
- Runs: 0.00 MB
- Total: 4.24 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
