# WS4 tiled 30-m dataset — N2|BC|S33

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `N2|BC|S33` (parent `N2|BC`)
- Tile / row / col: `N2` / 3 / 3
- Province: `BC`
- Centroid: 58.268691, -133.321030
- Allocated harvest: 130.037610 m3
- Productive subcell area: 320.069706 ha
- Committed geometry area: 1519.021519 ha
- Clipped inventory geometry: 1519.021519 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 900
- Blocks: 563
- Forest area: 81.00 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 314
- Scheduled area: 37.17 ha
- Eligible blocks (age class >= 40): 314
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 0.08 MB
- Schedules: 0.00 MB
- Runs: 0.00 MB
- Total: 0.09 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
