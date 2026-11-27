# WS4 tiled 30-m dataset — P2|BC|S23

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `P2|BC|S23` (parent `P2|BC`)
- Tile / row / col: `P2` / 2 / 3
- Province: `BC`
- Centroid: 59.934804, -136.508561
- Allocated harvest: 1794.921447 m3
- Productive subcell area: 5545.557424 ha
- Committed geometry area: 47028.568547 ha
- Clipped inventory geometry: 47028.568547 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 38645
- Blocks: 23795
- Forest area: 3478.05 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 1735
- Scheduled area: 232.20 ha
- Eligible blocks (age class >= 40): 17348
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 0.83 MB
- Schedules: 0.02 MB
- Runs: 0.00 MB
- Total: 0.85 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
