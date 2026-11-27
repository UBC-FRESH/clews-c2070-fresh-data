# WS4 tiled 30-m dataset — M29|NL|S21

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `M29|NL|S21` (parent `M29|NL`)
- Tile / row / col: `M29` / 2 / 1
- Province: `NL`
- Centroid: 57.767117, -61.727773
- Allocated harvest: 313.508346 m3
- Productive subcell area: 3626.738684 ha
- Committed geometry area: 9575.256213 ha
- Clipped inventory geometry: 9575.256213 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1443
- Blocks: 875
- Forest area: 129.87 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 94
- Scheduled area: 10.17 ha
- Eligible blocks (age class >= 40): 94
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 0.09 MB
- Schedules: 0.00 MB
- Runs: 0.00 MB
- Total: 0.09 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
