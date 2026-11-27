# WS4 tiled 30-m dataset — N6|BC|S11

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `N6|BC|S11` (parent `N6|BC`)
- Tile / row / col: `N6` / 1 / 1
- Province: `BC`
- Centroid: 59.821677, -125.247568
- Allocated harvest: 63844.280325 m3
- Productive subcell area: 194485.847569 ha
- Committed geometry area: 206942.379746 ha
- Clipped inventory geometry: 206942.379746 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2010477
- Blocks: 1003041
- Forest area: 180942.93 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 98010
- Scheduled area: 16896.60 ha
- Eligible blocks (age class >= 40): 980098
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 28.21 MB
- Schedules: 1.17 MB
- Runs: 0.00 MB
- Total: 29.37 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
