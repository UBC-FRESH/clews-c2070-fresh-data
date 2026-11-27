# WS4 tiled 30-m dataset — H18|MB|S31

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `H18|MB|S31` (parent `H18|MB`)
- Tile / row / col: `H18` / 3 / 1
- Province: `MB`
- Centroid: 55.980274, -91.494390
- Allocated harvest: 3092.255486 m3
- Productive subcell area: 153348.919272 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2034538
- Blocks: 551499
- Forest area: 183108.42 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 41691
- Scheduled area: 10661.31 ha
- Eligible blocks (age class >= 40): 416910
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 21.67 MB
- Schedules: 0.49 MB
- Runs: 0.00 MB
- Total: 22.16 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
