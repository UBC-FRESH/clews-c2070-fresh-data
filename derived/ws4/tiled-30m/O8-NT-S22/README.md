# WS4 tiled 30-m dataset — O8|NT|S22

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `O8|NT|S22` (parent `O8|NT`)
- Tile / row / col: `O8` / 2 / 2
- Province: `NT`
- Centroid: 62.915947, -120.779695
- Allocated harvest: 124.606406 m3
- Productive subcell area: 146971.298125 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1253702
- Blocks: 408967
- Forest area: 112833.18 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 19435
- Scheduled area: 3544.20 ha
- Eligible blocks (age class >= 40): 194341
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 14.65 MB
- Schedules: 0.23 MB
- Runs: 0.00 MB
- Total: 14.88 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
