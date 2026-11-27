# WS4 tiled 30-m dataset — P5|YT|S21

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `P5|YT|S21` (parent `P5|YT`)
- Tile / row / col: `P5` / 2 / 1
- Province: `YT`
- Centroid: 61.980376, -131.019302
- Allocated harvest: 178.544340 m3
- Productive subcell area: 176847.291549 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2334964
- Blocks: 870847
- Forest area: 210146.76 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 77284
- Scheduled area: 16766.91 ha
- Eligible blocks (age class >= 40): 772834
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 28.97 MB
- Schedules: 0.92 MB
- Runs: 0.00 MB
- Total: 29.89 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
