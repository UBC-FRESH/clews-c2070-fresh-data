# WS4 tiled 30-m dataset — G34|NL|S31

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `G34|NL|S31` (parent `G34|NL`)
- Tile / row / col: `G34` / 3 / 1
- Province: `NL`
- Centroid: 47.761098, -58.424946
- Allocated harvest: 3694.988399 m3
- Productive subcell area: 55674.490215 ha
- Committed geometry area: 121334.280588 ha
- Clipped inventory geometry: 121334.280588 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 326519
- Blocks: 210607
- Forest area: 29386.71 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 16621
- Scheduled area: 2408.04 ha
- Eligible blocks (age class >= 40): 166206
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 5.97 MB
- Schedules: 0.19 MB
- Runs: 0.00 MB
- Total: 6.16 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
