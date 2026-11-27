# WS4 tiled 30-m dataset — O5|YT|S21

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `O5|YT|S21` (parent `O5|YT`)
- Tile / row / col: `O5` / 2 / 1
- Province: `YT`
- Centroid: 60.801172, -129.497157
- Allocated harvest: 258.538255 m3
- Productive subcell area: 172813.327718 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2207010
- Blocks: 925627
- Forest area: 198630.90 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 83437
- Scheduled area: 16002.27 ha
- Eligible blocks (age class >= 40): 834367
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 28.56 MB
- Schedules: 0.99 MB
- Runs: 0.00 MB
- Total: 29.55 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
