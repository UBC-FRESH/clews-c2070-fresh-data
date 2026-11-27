# WS4 tiled 30-m dataset — G6|BC|S11

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `G6|BC|S11` (parent `G6|BC`)
- Tile / row / col: `G6` / 1 / 1
- Province: `BC`
- Centroid: 51.072671, -118.317561
- Allocated harvest: 104404.379749 m3
- Productive subcell area: 145787.906891 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2021694
- Blocks: 1073363
- Forest area: 181952.46 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 100491
- Scheduled area: 15520.77 ha
- Eligible blocks (age class >= 40): 1004904
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 28.72 MB
- Schedules: 1.20 MB
- Runs: 0.00 MB
- Total: 29.92 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
