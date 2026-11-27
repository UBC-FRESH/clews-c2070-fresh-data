# WS4 tiled 30-m dataset — E22|ON|S12

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `E22|ON|S12` (parent `E22|ON`)
- Tile / row / col: `E22` / 1 / 2
- Province: `ON`
- Centroid: 50.263306, -82.748631
- Allocated harvest: 25238.635475 m3
- Productive subcell area: 176992.444459 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2451245
- Blocks: 978267
- Forest area: 220612.05 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 92897
- Scheduled area: 20461.59 ha
- Eligible blocks (age class >= 40): 928965
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 31.39 MB
- Schedules: 1.10 MB
- Runs: 0.00 MB
- Total: 32.49 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
