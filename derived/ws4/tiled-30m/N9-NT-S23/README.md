# WS4 tiled 30-m dataset — N9|NT|S23

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `N9|NT|S23` (parent `N9|NT`)
- Tile / row / col: `N9` / 2 / 3
- Province: `NT`
- Centroid: 62.284878, -115.950187
- Allocated harvest: 111.035828 m3
- Productive subcell area: 95511.724318 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 496214
- Blocks: 190987
- Forest area: 44659.26 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 11198
- Scheduled area: 2554.47 ha
- Eligible blocks (age class >= 40): 111975
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 6.59 MB
- Schedules: 0.13 MB
- Runs: 0.00 MB
- Total: 6.72 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
