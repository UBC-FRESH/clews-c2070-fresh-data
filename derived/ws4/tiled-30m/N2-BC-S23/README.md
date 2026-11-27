# WS4 tiled 30-m dataset — N2|BC|S23

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `N2|BC|S23` (parent `N2|BC`)
- Tile / row / col: `N2` / 2 / 3
- Province: `BC`
- Centroid: 57.957714, -132.957372
- Allocated harvest: 1567.351116 m3
- Productive subcell area: 3857.819377 ha
- Committed geometry area: 18308.857543 ha
- Clipped inventory geometry: 18308.857543 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 4022
- Blocks: 2282
- Forest area: 361.98 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 1804
- Scheduled area: 260.19 ha
- Eligible blocks (age class >= 40): 1804
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 0.14 MB
- Schedules: 0.02 MB
- Runs: 0.00 MB
- Total: 0.16 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
