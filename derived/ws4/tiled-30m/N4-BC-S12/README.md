# WS4 tiled 30-m dataset — N4|BC|S12

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `N4|BC|S12` (parent `N4|BC`)
- Tile / row / col: `N4` / 1 / 2
- Province: `BC`
- Centroid: 58.742961, -129.185316
- Allocated harvest: 44279.454431 m3
- Productive subcell area: 151492.572394 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1407971
- Blocks: 782705
- Forest area: 126717.39 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 71347
- Scheduled area: 11062.44 ha
- Eligible blocks (age class >= 40): 713465
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 20.86 MB
- Schedules: 0.85 MB
- Runs: 0.00 MB
- Total: 21.71 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
