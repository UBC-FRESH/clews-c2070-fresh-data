# WS4 tiled 30-m dataset — N11|NT|S31

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `N11|NT|S31` (parent `N11|NT`)
- Tile / row / col: `N11` / 3 / 1
- Province: `NT`
- Centroid: 63.276275, -112.391997
- Allocated harvest: 42.605610 m3
- Productive subcell area: 75817.363283 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1358311
- Blocks: 459542
- Forest area: 122247.99 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 28872
- Scheduled area: 5195.34 ha
- Eligible blocks (age class >= 40): 288713
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 15.90 MB
- Schedules: 0.34 MB
- Runs: 0.00 MB
- Total: 16.24 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
