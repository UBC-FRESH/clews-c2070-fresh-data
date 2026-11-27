# WS4 tiled 30-m dataset — I10|SK|S22

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `I10|SK|S22` (parent `I10|SK`)
- Tile / row / col: `I10` / 2 / 2
- Province: `SK`
- Centroid: 55.777520, -109.981214
- Allocated harvest: 426.109374 m3
- Productive subcell area: 2201.891945 ha
- Committed geometry area: 2609.791733 ha
- Clipped inventory geometry: 2609.791733 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 28405
- Blocks: 7205
- Forest area: 2556.45 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 535
- Scheduled area: 128.07 ha
- Eligible blocks (age class >= 40): 5342
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 0.43 MB
- Schedules: 0.01 MB
- Runs: 0.00 MB
- Total: 0.44 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
