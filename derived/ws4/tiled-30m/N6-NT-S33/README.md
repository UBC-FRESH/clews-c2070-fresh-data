# WS4 tiled 30-m dataset — N6|NT|S33

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `N6|NT|S33` (parent `N6|NT`)
- Tile / row / col: `N6` / 3 / 3
- Province: `NT`
- Centroid: 61.117904, -124.403522
- Allocated harvest: 273.624692 m3
- Productive subcell area: 185966.069380 ha
- Committed geometry area: 235410.465874 ha
- Clipped inventory geometry: 235410.465874 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1739837
- Blocks: 563807
- Forest area: 156585.33 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 49028
- Scheduled area: 30471.66 ha
- Eligible blocks (age class >= 40): 490271
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 19.72 MB
- Schedules: 0.58 MB
- Runs: 0.00 MB
- Total: 20.30 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
