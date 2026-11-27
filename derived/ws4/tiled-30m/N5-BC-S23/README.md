# WS4 tiled 30-m dataset — N5|BC|S23

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `N5|BC|S23` (parent `N5|BC`)
- Tile / row / col: `N5` / 2 / 3
- Province: `BC`
- Centroid: 59.912908, -126.459459
- Allocated harvest: 26077.052249 m3
- Productive subcell area: 80817.716751 ha
- Committed geometry area: 91206.377216 ha
- Clipped inventory geometry: 91206.377216 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 980560
- Blocks: 281428
- Forest area: 88250.40 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 27736
- Scheduled area: 5613.48 ha
- Eligible blocks (age class >= 40): 277352
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 10.67 MB
- Schedules: 0.32 MB
- Runs: 0.00 MB
- Total: 10.99 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
