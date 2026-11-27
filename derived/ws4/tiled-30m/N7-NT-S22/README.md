# WS4 tiled 30-m dataset — N7|NT|S22

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `N7|NT|S22` (parent `N7|NT`)
- Tile / row / col: `N7` / 2 / 2
- Province: `NT`
- Centroid: 61.085497, -122.282058
- Allocated harvest: 283.888167 m3
- Productive subcell area: 199348.083161 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2501151
- Blocks: 1020667
- Forest area: 225103.59 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 98166
- Scheduled area: 20101.23 ha
- Eligible blocks (age class >= 40): 981654
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 32.43 MB
- Schedules: 1.17 MB
- Runs: 0.00 MB
- Total: 33.60 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
