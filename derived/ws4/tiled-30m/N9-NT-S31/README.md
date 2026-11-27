# WS4 tiled 30-m dataset — N9|NT|S31

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `N9|NT|S31` (parent `N9|NT`)
- Tile / row / col: `N9` / 3 / 1
- Province: `NT`
- Centroid: 62.405522, -118.160085
- Allocated harvest: 111.035828 m3
- Productive subcell area: 95511.724318 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1328498
- Blocks: 389467
- Forest area: 119564.82 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 18550
- Scheduled area: 2861.10 ha
- Eligible blocks (age class >= 40): 185493
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 14.69 MB
- Schedules: 0.22 MB
- Runs: 0.00 MB
- Total: 14.91 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
