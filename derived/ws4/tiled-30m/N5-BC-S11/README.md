# WS4 tiled 30-m dataset — N5|BC|S11

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `N5|BC|S11` (parent `N5|BC`)
- Tile / row / col: `N5` / 1 / 1
- Province: `BC`
- Centroid: 59.205498, -127.639937
- Allocated harvest: 71478.149458 m3
- Productive subcell area: 221524.303503 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2348808
- Blocks: 1108449
- Forest area: 211392.72 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 102627
- Scheduled area: 17740.53 ha
- Eligible blocks (age class >= 40): 1026268
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 32.49 MB
- Schedules: 1.23 MB
- Runs: 0.00 MB
- Total: 33.72 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
