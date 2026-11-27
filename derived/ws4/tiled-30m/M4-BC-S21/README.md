# WS4 tiled 30-m dataset — M4|BC|S21

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `M4|BC|S21` (parent `M4|BC`)
- Tile / row / col: `M4` / 2 / 1
- Province: `BC`
- Centroid: 57.715641, -129.043500
- Allocated harvest: 93682.180011 m3
- Productive subcell area: 139942.345505 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1436532
- Blocks: 672594
- Forest area: 129287.88 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 59961
- Scheduled area: 10466.91 ha
- Eligible blocks (age class >= 40): 599607
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 19.79 MB
- Schedules: 0.71 MB
- Runs: 0.00 MB
- Total: 20.50 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
