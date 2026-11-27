# WS4 tiled 30-m dataset — N7|NT|S13

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `N7|NT|S13` (parent `N7|NT`)
- Tile / row / col: `N7` / 1 / 3
- Province: `NT`
- Centroid: 60.851385, -121.026698
- Allocated harvest: 283.888167 m3
- Productive subcell area: 199348.083161 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2289735
- Blocks: 648292
- Forest area: 206076.15 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 61276
- Scheduled area: 19660.86 ha
- Eligible blocks (age class >= 40): 612759
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 26.13 MB
- Schedules: 0.73 MB
- Runs: 0.00 MB
- Total: 26.85 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
