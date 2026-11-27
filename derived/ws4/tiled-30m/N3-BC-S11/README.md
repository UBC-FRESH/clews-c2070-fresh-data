# WS4 tiled 30-m dataset — N3|BC|S11

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `N3|BC|S11` (parent `N3|BC`)
- Tile / row / col: `N3` / 1 / 1
- Province: `BC`
- Centroid: 57.762769, -132.145822
- Allocated harvest: 58302.470601 m3
- Productive subcell area: 134469.950102 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 756598
- Blocks: 440776
- Forest area: 68093.82 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 39012
- Scheduled area: 5527.26 ha
- Eligible blocks (age class >= 40): 390111
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 11.74 MB
- Schedules: 0.46 MB
- Runs: 0.00 MB
- Total: 12.20 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
