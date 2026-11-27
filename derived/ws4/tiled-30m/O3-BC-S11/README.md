# WS4 tiled 30-m dataset — O3|BC|S11

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `O3|BC|S11` (parent `O3|BC`)
- Tile / row / col: `O3` / 1 / 1
- Province: `BC`
- Centroid: 58.913560, -133.614604
- Allocated harvest: 54864.294018 m3
- Productive subcell area: 134784.350605 ha
- Committed geometry area: 243131.560887 ha
- Clipped inventory geometry: 243131.560887 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 889023
- Blocks: 505785
- Forest area: 80012.07 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 45272
- Scheduled area: 6881.94 ha
- Eligible blocks (age class >= 40): 452716
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 13.53 MB
- Schedules: 0.53 MB
- Runs: 0.00 MB
- Total: 14.06 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
