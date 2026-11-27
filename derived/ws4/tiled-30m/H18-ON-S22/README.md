# WS4 tiled 30-m dataset — H18|ON|S22

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `H18|ON|S22` (parent `H18|ON`)
- Tile / row / col: `H18` / 2 / 2
- Province: `ON`
- Centroid: 55.476356, -90.701181
- Allocated harvest: 9466.325419 m3
- Productive subcell area: 118351.662494 ha
- Committed geometry area: 224623.422107 ha
- Clipped inventory geometry: 224623.422107 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1500862
- Blocks: 626857
- Forest area: 135077.58 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 53614
- Scheduled area: 11264.49 ha
- Eligible blocks (age class >= 40): 536134
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 19.62 MB
- Schedules: 0.63 MB
- Runs: 0.00 MB
- Total: 20.26 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
