# WS4 tiled 30-m dataset — G6|BC|S22

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `G6|BC|S22` (parent `G6|BC`)
- Tile / row / col: `G6` / 2 / 2
- Province: `BC`
- Centroid: 51.657426, -117.898053
- Allocated harvest: 104404.379749 m3
- Productive subcell area: 145787.906891 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1358722
- Blocks: 687623
- Forest area: 122284.98 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 63317
- Scheduled area: 10092.51 ha
- Eligible blocks (age class >= 40): 633163
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 19.23 MB
- Schedules: 0.75 MB
- Runs: 0.00 MB
- Total: 19.98 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
