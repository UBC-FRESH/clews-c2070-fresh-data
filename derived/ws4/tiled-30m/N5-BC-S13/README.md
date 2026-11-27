# WS4 tiled 30-m dataset — N5|BC|S13

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `N5|BC|S13` (parent `N5|BC`)
- Tile / row / col: `N5` / 1 / 3
- Province: `BC`
- Centroid: 59.648491, -126.051060
- Allocated harvest: 71478.149458 m3
- Productive subcell area: 221524.303503 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2610902
- Blocks: 992042
- Forest area: 234981.18 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 95524
- Scheduled area: 18737.64 ha
- Eligible blocks (age class >= 40): 955236
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 31.62 MB
- Schedules: 1.14 MB
- Runs: 0.00 MB
- Total: 32.75 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
