# WS4 tiled 30-m dataset — R8|NT|S21

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `R8|NT|S21` (parent `R8|NT`)
- Tile / row / col: `R8` / 2 / 1
- Province: `NT`
- Centroid: 66.474962, -125.952625
- Allocated harvest: 54.117985 m3
- Productive subcell area: 151558.072555 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1784429
- Blocks: 570983
- Forest area: 160598.61 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 46124
- Scheduled area: 11771.46 ha
- Eligible blocks (age class >= 40): 461240
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 20.38 MB
- Schedules: 0.54 MB
- Runs: 0.00 MB
- Total: 20.92 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
