# WS4 tiled 30-m dataset — N5|YT|S33

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `N5|YT|S33` (parent `N5|YT`)
- Tile / row / col: `N5` / 3 / 3
- Province: `YT`
- Centroid: 60.460657, -126.928748
- Allocated harvest: 515.521257 m3
- Productive subcell area: 218255.869305 ha
- Committed geometry area: 249638.731813 ha
- Clipped inventory geometry: 249638.731813 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2417617
- Blocks: 1070977
- Forest area: 217585.53 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 100531
- Scheduled area: 19016.28 ha
- Eligible blocks (age class >= 40): 1005304
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 31.85 MB
- Schedules: 1.20 MB
- Runs: 0.00 MB
- Total: 33.06 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
