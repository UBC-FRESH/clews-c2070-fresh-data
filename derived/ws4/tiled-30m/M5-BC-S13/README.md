# WS4 tiled 30-m dataset — M5|BC|S13

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `M5|BC|S13` (parent `M5|BC`)
- Tile / row / col: `M5` / 1 / 3
- Province: `BC`
- Centroid: 58.420285, -124.815218
- Allocated harvest: 44439.105201 m3
- Productive subcell area: 135935.973745 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 465511
- Blocks: 216263
- Forest area: 41895.99 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 17904
- Scheduled area: 3541.77 ha
- Eligible blocks (age class >= 40): 179034
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 6.97 MB
- Schedules: 0.21 MB
- Runs: 0.00 MB
- Total: 7.17 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
