# WS4 tiled 30-m dataset — N6|YT|S12

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `N6|YT|S12` (parent `N6|YT`)
- Tile / row / col: `N6` / 1 / 2
- Province: `YT`
- Centroid: 60.141855, -124.450513
- Allocated harvest: 325.768886 m3
- Productive subcell area: 137180.543681 ha
- Committed geometry area: 158455.776853 ha
- Clipped inventory geometry: 158455.776853 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1567162
- Blocks: 781624
- Forest area: 141044.58 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 73522
- Scheduled area: 12356.28 ha
- Eligible blocks (age class >= 40): 735216
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 22.27 MB
- Schedules: 0.87 MB
- Runs: 0.00 MB
- Total: 23.14 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
