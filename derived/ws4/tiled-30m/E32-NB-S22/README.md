# WS4 tiled 30-m dataset — E32|NB|S22

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `E32|NB|S22` (parent `E32|NB`)
- Tile / row / col: `E32` / 2 / 2
- Province: `NB`
- Centroid: 46.107769, -63.840857
- Allocated harvest: 3206.771376 m3
- Productive subcell area: 4697.355932 ha
- Committed geometry area: 6009.986353 ha
- Clipped inventory geometry: 6009.986353 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 49597
- Blocks: 17356
- Forest area: 4463.73 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 1240
- Scheduled area: 255.78 ha
- Eligible blocks (age class >= 40): 12398
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 0.80 MB
- Schedules: 0.01 MB
- Runs: 0.00 MB
- Total: 0.82 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
