# WS4 tiled 30-m dataset — E22|ON|S31

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `E22|ON|S31` (parent `E22|ON`)
- Tile / row / col: `E22` / 3 / 1
- Province: `ON`
- Centroid: 51.236972, -83.180716
- Allocated harvest: 25238.635475 m3
- Productive subcell area: 176992.444459 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1339816
- Blocks: 438001
- Forest area: 120583.44 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 38980
- Scheduled area: 11320.74 ha
- Eligible blocks (age class >= 40): 389793
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 16.11 MB
- Schedules: 0.46 MB
- Runs: 0.00 MB
- Total: 16.57 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
