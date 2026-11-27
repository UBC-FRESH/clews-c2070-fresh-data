# WS4 tiled 30-m dataset — N5|BC|S22

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `N5|BC|S22` (parent `N5|BC`)
- Tile / row / col: `N5` / 2 / 2
- Province: `BC`
- Centroid: 59.804255, -127.298917
- Allocated harvest: 62927.321787 m3
- Productive subcell area: 195023.671372 ha
- Committed geometry area: 220092.861470 ha
- Clipped inventory geometry: 220092.861470 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2294114
- Blocks: 549215
- Forest area: 206470.26 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 51802
- Scheduled area: 16186.86 ha
- Eligible blocks (age class >= 40): 518020
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 22.60 MB
- Schedules: 0.61 MB
- Runs: 0.00 MB
- Total: 23.21 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
