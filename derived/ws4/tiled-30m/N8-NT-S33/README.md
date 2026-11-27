# WS4 tiled 30-m dataset — N8|NT|S33

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `N8|NT|S33` (parent `N8|NT`)
- Tile / row / col: `N8` / 3 / 3
- Province: `NT`
- Centroid: 62.237665, -119.086550
- Allocated harvest: 173.224674 m3
- Productive subcell area: 141366.160040 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1303656
- Blocks: 419902
- Forest area: 117329.04 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 22635
- Scheduled area: 4042.26 ha
- Eligible blocks (age class >= 40): 226344
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 14.81 MB
- Schedules: 0.27 MB
- Runs: 0.00 MB
- Total: 15.08 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
