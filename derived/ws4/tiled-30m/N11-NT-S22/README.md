# WS4 tiled 30-m dataset — N11|NT|S22

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `N11|NT|S22` (parent `N11|NT`)
- Tile / row / col: `N11` / 2 / 2
- Province: `NT`
- Centroid: 62.950150, -111.139523
- Allocated harvest: 42.605610 m3
- Productive subcell area: 75817.363283 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 932915
- Blocks: 460664
- Forest area: 83962.35 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 28776
- Scheduled area: 5636.61 ha
- Eligible blocks (age class >= 40): 287760
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 12.92 MB
- Schedules: 0.34 MB
- Runs: 0.00 MB
- Total: 13.26 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
