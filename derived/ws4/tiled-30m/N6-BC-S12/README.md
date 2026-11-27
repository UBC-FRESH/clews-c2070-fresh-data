# WS4 tiled 30-m dataset — N6|BC|S12

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `N6|BC|S12` (parent `N6|BC`)
- Tile / row / col: `N6` / 1 / 2
- Province: `BC`
- Centroid: 59.919496, -124.397639
- Allocated harvest: 25398.531538 m3
- Productive subcell area: 77370.359693 ha
- Committed geometry area: 82325.817312 ha
- Clipped inventory geometry: 82325.817312 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 896474
- Blocks: 443417
- Forest area: 80682.66 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 42903
- Scheduled area: 6838.56 ha
- Eligible blocks (age class >= 40): 429024
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 12.75 MB
- Schedules: 0.50 MB
- Runs: 0.00 MB
- Total: 13.25 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
