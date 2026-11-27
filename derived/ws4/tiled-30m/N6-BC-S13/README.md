# WS4 tiled 30-m dataset — N6|BC|S13

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `N6|BC|S13` (parent `N6|BC`)
- Tile / row / col: `N6` / 1 / 3
- Province: `BC`
- Centroid: 59.988746, -123.765465
- Allocated harvest: 537.359257 m3
- Productive subcell area: 1636.932393 ha
- Committed geometry area: 1741.775503 ha
- Clipped inventory geometry: 1741.775503 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 17071
- Blocks: 9759
- Forest area: 1536.39 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 951
- Scheduled area: 141.84 ha
- Eligible blocks (age class >= 40): 9501
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 0.39 MB
- Schedules: 0.01 MB
- Runs: 0.00 MB
- Total: 0.40 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
