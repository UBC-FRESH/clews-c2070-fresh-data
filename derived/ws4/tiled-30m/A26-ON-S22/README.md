# WS4 tiled 30-m dataset — A26|ON|S22

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `A26|ON|S22` (parent `A26|ON`)
- Tile / row / col: `A26` / 2 / 2
- Province: `ON`
- Centroid: 44.271000, -76.843465
- Allocated harvest: 24158.394705 m3
- Productive subcell area: 96204.111997 ha
- Committed geometry area: 177532.633904 ha
- Clipped inventory geometry: 177532.633904 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 769236
- Blocks: 348856
- Forest area: 69231.24 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 26137
- Scheduled area: 5469.66 ha
- Eligible blocks (age class >= 40): 261366
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 10.70 MB
- Schedules: 0.31 MB
- Runs: 0.00 MB
- Total: 11.00 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
