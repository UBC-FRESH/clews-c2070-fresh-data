# WS4 tiled 30-m dataset — N3|BC|S23

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `N3|BC|S23` (parent `N3|BC`)
- Tile / row / col: `N3` / 2 / 3
- Province: `BC`
- Centroid: 58.651015, -131.157782
- Allocated harvest: 58302.470601 m3
- Productive subcell area: 134469.950102 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1447960
- Blocks: 774373
- Forest area: 130316.40 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 69416
- Scheduled area: 11355.03 ha
- Eligible blocks (age class >= 40): 694154
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 21.15 MB
- Schedules: 0.82 MB
- Runs: 0.00 MB
- Total: 21.98 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
