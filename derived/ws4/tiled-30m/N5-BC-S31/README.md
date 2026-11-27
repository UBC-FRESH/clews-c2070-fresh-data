# WS4 tiled 30-m dataset — N5|BC|S31

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `N5|BC|S31` (parent `N5|BC`)
- Tile / row / col: `N5` / 3 / 1
- Province: `BC`
- Centroid: 59.892090, -128.519083
- Allocated harvest: 34685.120223 m3
- Productive subcell area: 107495.747406 ha
- Committed geometry area: 121313.717848 ha
- Clipped inventory geometry: 121313.717848 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1240605
- Blocks: 592290
- Forest area: 111654.45 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 56160
- Scheduled area: 8750.70 ha
- Eligible blocks (age class >= 40): 561595
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 17.25 MB
- Schedules: 0.66 MB
- Runs: 0.00 MB
- Total: 17.91 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
