# WS4 tiled 30-m dataset — N6|NT|S32

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `N6|NT|S32` (parent `N6|NT`)
- Tile / row / col: `N6` / 3 / 2
- Province: `NT`
- Centroid: 60.965419, -125.308014
- Allocated harvest: 195.958392 m3
- Productive subcell area: 133181.007139 ha
- Committed geometry area: 168590.985660 ha
- Clipped inventory geometry: 168590.985660 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1543863
- Blocks: 575431
- Forest area: 138947.67 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 52844
- Scheduled area: 14002.56 ha
- Eligible blocks (age class >= 40): 528432
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 18.78 MB
- Schedules: 0.62 MB
- Runs: 0.00 MB
- Total: 19.41 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
